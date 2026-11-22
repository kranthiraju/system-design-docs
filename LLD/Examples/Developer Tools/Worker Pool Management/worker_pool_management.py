
import uuid
import time
import threading
import queue

from datetime import datetime
from enum import Enum


# ---------------- ENUMS ----------------

class JobStatus(Enum):
    NOT_STARTED = "NOT_STARTED"
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


class WorkerStatus(Enum):
    IDLE = "IDLE"
    BUSY = "BUSY"
    UNAVAILABLE = "UNAVAILABLE"


class ExecutionStatus(Enum):
    RUNNING = "RUNNING"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"


# ---------------- JOB EXECUTION ----------------

class JobExecution:

    def __init__(self, job_id, worker_id):
        self.execution_id = uuid.uuid4()
        self.job_id = job_id
        self.worker_id = worker_id

        self.started_at = datetime.now()
        self.completed_at = None

        self.status = ExecutionStatus.RUNNING
        self.error_message = ""


# ---------------- JOB ----------------

class Job:

    def __init__(self, action):
        self.job_id = uuid.uuid4()
        self.action = action

        self.created_at = datetime.now()
        self.status = JobStatus.NOT_STARTED

        self.execution_history = []

    def execute(self):
        self.action()


# ---------------- JOB QUEUE ----------------

class JobQueue:

    def __init__(self, condition):
        self.jobs = queue.Queue()
        self.condition = condition

    def add_job(self, job):

        with self.condition:

            self.jobs.put(job)

            print(f"[QUEUE] Job added: {job.job_id}")
            print(f"[QUEUE] Pending jobs: {self.jobs.qsize()}")

            self.condition.notify()

    def get_job(self):

        if not self.jobs.empty():
            return self.jobs.get()

        return None

    def is_empty(self):
        return self.jobs.empty()


# ---------------- WORKER ----------------

class Worker:

    def __init__(self, condition, job_queue, shutdown_event):

        self.worker_id = uuid.uuid4()

        self.current_job = None
        self.status = WorkerStatus.IDLE

        self.worker_thread = None

        self.condition = condition
        self.job_queue = job_queue
        self.shutdown_event = shutdown_event

    def run(self):

        self.worker_thread = threading.Thread(
            target=self.execute_job,
            name=f"Worker-{str(self.worker_id)[:8]}"
        )

        self.worker_thread.start()

        print(f"[WORKER] Started: {self.worker_id}")

    def execute_job(self):

        while True:

            with self.condition:

                # Wait while queue is empty and shutdown isn't requested
                while (
                    self.job_queue.is_empty()
                    and not self.shutdown_event.is_set()
                ):
                    self.status = WorkerStatus.IDLE

                    print(f"[WORKER {self.worker_id}] Waiting for jobs")

                    self.condition.wait()

                # Graceful shutdown:
                # Exit only when shutdown is requested
                # and all pending jobs have been processed.
                if (
                    self.shutdown_event.is_set()
                    and self.job_queue.is_empty()
                ):
                    self.status = WorkerStatus.UNAVAILABLE

                    print(f"[WORKER {self.worker_id}] Shutting down")
                    return

                job = self.job_queue.get_job()

            # Execute outside the condition lock
            if job:
                self.current_job = job
                self._execution()

    def _execution(self):

        job = self.current_job

        self.status = WorkerStatus.BUSY
        job.status = JobStatus.RUNNING

        execution = JobExecution(
            job.job_id,
            self.worker_id
        )

        job.execution_history.append(execution)

        print(
            f"[EXECUTION STARTED] "
            f"Worker: {self.worker_id} | Job: {job.job_id}"
        )

        try:

            job.execute()

            job.status = JobStatus.COMPLETED
            execution.status = ExecutionStatus.SUCCESS

            print(
                f"[EXECUTION COMPLETED] "
                f"Worker: {self.worker_id} | Job: {job.job_id}"
            )

        except Exception as error:

            job.status = JobStatus.FAILED

            execution.status = ExecutionStatus.FAILED
            execution.error_message = str(error)

            print(
                f"[EXECUTION FAILED] "
                f"Worker: {self.worker_id} | "
                f"Error: {error}"
            )

        finally:

            execution.completed_at = datetime.now()

            self.current_job = None
            self.status = WorkerStatus.IDLE

            print(
                f"[WORKER {self.worker_id}] "
                f"Available for next job"
            )


# ---------------- WORKER POOL MANAGER ----------------

class WorkerPoolManagement:

    def __init__(self, max_workers=3):

        self.max_workers = max_workers

        self.condition = threading.Condition()

        self.shutdown_event = threading.Event()

        self.job_queue = JobQueue(self.condition)

        self.workers = []

        self.started = False

    def start(self):

        if self.started:
            return

        self.started = True

        print("[MANAGER] Starting worker pool")

        for _ in range(self.max_workers):

            worker = Worker(
                self.condition,
                self.job_queue,
                self.shutdown_event
            )

            worker.run()

            self.workers.append(worker)

    def submit_job(self, job: Job):

        if self.shutdown_event.is_set():
            raise RuntimeError("Worker pool is shutting down")

        if not self.started:
            raise RuntimeError("Start the worker pool first")

        self.job_queue.add_job(job)

    def stop(self):

        if not self.started:
            return

        print("[MANAGER] Graceful shutdown initiated")

        # Signal all workers to stop after pending jobs finish
        with self.condition:

            self.shutdown_event.set()

            self.condition.notify_all()

        # Wait for all workers to finish
        for worker in self.workers:
            worker.worker_thread.join()

        self.started = False

        print("[MANAGER] All workers stopped")
