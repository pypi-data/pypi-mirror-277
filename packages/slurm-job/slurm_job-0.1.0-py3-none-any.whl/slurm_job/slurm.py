"""For slurm related code"""

import argparse
import datetime
import logging
import time
import uuid
from functools import wraps
from pathlib import Path
from typing import Any, Callable, Optional, TypedDict, Union

import rich
import sh
from simple_slurm import Slurm
from watchdog.events import FileSystemEvent, FileSystemEventHandler
from watchdog.observers import Observer

from slurm_job.core import FunctionCall, Job, Template
from slurm_job.utils import tail_output

logger = logging.getLogger(__name__)


class SlurmOptions(TypedDict, total=False):
    """Type definition for Slurm options."""

    account: str
    acctg_freq: str
    array: str
    batch: str
    bb: str
    bbf: str
    begin: str
    chdir: str
    cluster_constraint: str
    clusters: str
    comment: str
    constraint: str
    container: str
    container_id: str
    contiguous: bool
    core_spec: int
    cores_per_socket: int
    cpu_freq: str
    cpus_per_gpu: int
    cpus_per_task: int
    deadline: str
    delay_boot: int
    dependency: str
    distribution: str
    error: str
    exclude: str
    exclusive: str
    export: str
    export_file: str
    extra: str
    extra_node_info: str
    get_user_env: str
    gid: str
    gpu_bind: str
    gpu_freq: str
    gpus: str
    gpus_per_node: str
    gpus_per_socket: str
    gpus_per_task: str
    gres: str
    gres_flags: str
    hold: bool
    ignore_pbs: bool
    input: str
    job_name: str
    kill_on_invalid_dep: str
    licenses: str
    mail_type: str
    mail_user: str
    mcs_label: str
    mem: str
    mem_bind: str
    mem_per_cpu: str
    mem_per_gpu: str
    mincpus: int
    network: str
    nice: int
    no_kill: bool
    no_requeue: bool
    nodefile: str
    nodelist: str
    nodes: str
    ntasks: int
    ntasks_per_core: int
    ntasks_per_gpu: int
    ntasks_per_node: int
    ntasks_per_socket: int
    open_mode: str
    output: str
    overcommit: bool
    partition: str
    power: str
    prefer: str
    priority: str
    profile: str
    propagate: str
    qos: str
    quiet: bool
    reboot: bool
    requeue: bool
    reservation: str
    signal: str
    sockets_per_node: int
    spread_job: bool
    switches: str
    test_only: bool
    thread_spec: int
    threads_per_core: int
    time: str
    time_min: str
    tmp: str
    tres_per_task: str
    uid: str
    use_min_nodes: bool
    verbose: bool
    wait: bool
    wait_all_nodes: int
    wckey: str
    wrap: str


class SlurmError(Exception):
    """Exception raised for errors in the slurm job."""


class SlurmJob(Job):
    """Class to manage a slurm job."""

    def __init__(
        self,
        function_call: FunctionCall,
        script_template: Union[str, Template] = Template(),
        timeout: datetime.timedelta = datetime.timedelta(minutes=10),
        options: SlurmOptions = SlurmOptions(),
        watchdog_dir: Optional[Path] = None,
    ):
        super().__init__(function_call, script_template, timeout)
        self.options = options
        self.name = self.options.get("job_name", self.function_call.func.__name__)
        self.watchdog_dir = watchdog_dir

    def _submit_sbatch(self, job: Slurm) -> None:
        """Submit the job using sbatch."""
        self.id = job.sbatch()
        self.status.set_start()

    def _submit_watchdog(self, job: Slurm) -> None:
        """Submit the job using the watchdog."""
        target_dir = self.watchdog_dir or Path("slurm_jobs")
        if self.watchdog_dir and not self.watchdog_dir.exists():
            target_dir.mkdir(parents=True)
        elif self.watchdog_dir and not self.watchdog_dir.is_dir():
            raise ValueError(f"{self.watchdog_dir} is not a directory")
        # generate a unique filename
        script_file = target_dir / f"slurm-{uuid.uuid4()}.sh"
        script_file.write_text(job.script(), encoding="utf-8")
        id_file = script_file.with_suffix(".id")
        while not id_file.exists():
            time.sleep(0.5)
        self.id = int(id_file.read_text(encoding="utf-8").strip())
        id_file.unlink()
        if self.id < 1:
            raise SlurmError(f"Error submitting job:\n{job.script()}")

    def submit(self) -> int:
        """Submit the job."""
        has_sbatch = bool(sh.Command("which")("sbatch", _ok_code=[0, 1]))
        job = Slurm(**self.options)
        job.add_cmd("bash", "-c", self.script)
        if has_sbatch:
            self._submit_sbatch(job)
        else:
            self._submit_watchdog(job)
        return self.id

    def run(self) -> Any:
        """Run the job and return the result."""
        self.submit()
        output_file = Path(self.options.get("output", f"slurm-{self.id}.out"))
        if output_file.exists():
            output_file.unlink()  # remove the file if it already exists
        finished_event = tail_output(output_file, f"slurm-{self.id}-{self.name}")
        result = self.result()

        finished_event.wait()

        return result


def slurm_job(
    options: SlurmOptions = SlurmOptions(),
    script_template: Union[str, Template] = Template(),
    timeout: datetime.timedelta = datetime.timedelta(minutes=10),
    wait: bool = True,
):
    """
    Decorator to submit a function as a Slurm job.

    Args:
        options (SlurmOptions, optional): Slurm options. Defaults to SlurmOptions().
        script_template (Union[str, Template], optional): Template for job script.
                Defaults to Template().
        timeout (datetime.timedelta, optional): Timeout. Defaults to datetime.timedelta(minutes=10).
        wait (bool, optional): Set to False to return with job id immediately after submit.
                Defaults to True.

    Returns:
        Callable[..., Any]: Decorated function.
    """

    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            function_call = FunctionCall(func, args, kwargs)
            job = SlurmJob(function_call, script_template, timeout, options)
            if wait:
                return job.run()
            output_file = Path(options.get("output", f"slurm-{job.id}.out"))
            job_id = job.submit()
            rich.print(f"Submitted job {job_id} for {func.__name__}")
            rich.print(f"Logging output to {output_file.absolute()}")
            rich.print(f"Return value will be pickled to {job.return_path.absolute()}")
            return job_id

        return wrapper

    return decorator


class SlurmJobHandler(FileSystemEventHandler):
    """Handler for the watchdog managed slurm jobs."""

    def on_created(self, event: FileSystemEvent) -> None:
        if not event.is_directory and event.src_path.endswith(".sh"):
            file = Path(event.src_path)
            rich.print(f"Submitting {file}")
            job_id = 0
            id_file = file.with_suffix(".id")
            try:
                job_id = int(sh.Command("sbatch")(file).split()[-1])  # type: ignore
                rich.print("Submitted job", job_id, "for", file)
            except sh.ErrorReturnCode as e:
                rich.print(e.stderr)
            finally:
                id_file.write_text(str(job_id), encoding="utf-8")
                file.unlink()


def watch_slurm_jobs(target_dir: Path = Path("slurm_jobs")) -> None:
    """Watching slurm jobs in the target directory using watchdog."""
    if not target_dir.exists():
        target_dir.mkdir(parents=True)
    rich.print("Listening for slurm jobs in", target_dir, "using watchdog...")

    event_handler = SlurmJobHandler()
    observer = Observer()
    observer.schedule(event_handler, str(target_dir), recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


def main() -> None:
    """Entry point for the command line interface."""

    parser = argparse.ArgumentParser(description="Submit a function as a Slurm job")
    parser.add_argument("directory", type=Path, help="Directory to watch for slurm jobs")
    args = parser.parse_args()

    watch_slurm_jobs(args.directory)
