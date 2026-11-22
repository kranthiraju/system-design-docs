import time
import uuid
import threading
from enum import Enum
import heapq

from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

# Enums
class TaskType(Enum):
    ONE_TIME="ONE_TIME"
    RECURRING="RECURRING"

class TaskStatus(Enum):
    SCHEDULED="SCHEDULED"
    RUNNING="RUNNING"
    COMPLETED="COMPLETED"
    FAILED="FAILED"
    CANCELLED="CANCELLED"

class ExecutionStatus(Enum):
    RUNNING="RUNNING"
    SUCCESS="SUCCESS"
    FAILED="FAILED"

# Classes
class TaskExecution:
    def __init__(self, task_id):
        self.execution_id = f"exe_{uuid.uuid4()}"
        self.task_id = task_id
        self.started_at = datetime.now()
        self.completed_at = None
        self.status = ExecutionStatus.RUNNING
        self.error_message = ""

    def __str__(self):
        return f"{self.execution_id} - {self.task_id} - {self.started_at} - {self.completed_at} - {self.status} - {self.error_message}"


class Task:
    def __init__(self, name, action, task_type: TaskType, delay):
        self.task_id = str(uuid.uuid4())
        self.name = name
        self.action = action
        self.task_type = task_type
        self.created_time = datetime.now()
        self.schedule_time = time.time() + delay
        self.status = TaskStatus.SCHEDULED
        self.execution_history = []

    def execute(self):
        print(f"=========== {self.name} - {datetime.now()} ===========")
        self.action()

    def cancel(self):
        pass


class TaskScheduler:
    def __init__(self):
        self.task_queue = []
        self.cancelled_tasks = set()
        self.running=False

        self.scheduler_thread = None
        self.lock = threading.Lock()

        self.executor_worker = ThreadPoolExecutor(max_workers=3)

    def scheduleTask(self,task):
        with self.lock:
            heapq.heappush(self.task_queue, (
                task.schedule_time,
                task.task_id,
                task
            ))

    def cancelTask(self, task_id):
        with self.lock:
            self.cancelled_tasks.add(task_id)

    def start(self):
        if self.running:
            return

        self.running = True

        self.scheduler_thread = threading.Thread(
            target=self._run_scheduler,
            daemon=True
        )

        self.scheduler_thread.start()
        print(f"========== Task Scheduler Started : {datetime.now()} ==========")


    def _run_scheduler(self):
        while self.running:
            task = None
            with self.lock:
                if self.task_queue:
                    schedule_time, _, candidate = self.task_queue[0]
                    current_time = time.time()

                    if schedule_time <= current_time:
                        _,_,task = heapq.heappop(self.task_queue)

                        if task.task_id in self.cancelled_tasks:
                            task.status = TaskStatus.CANCELLED
                            task=None

            # Lock release here
            if task:
                task.status = TaskStatus.RUNNING
                # self._execute_task(task)
                self.executor_worker.submit(self._execute_task, task)
            else:
                time.sleep(0.1)

    def _execute_task(self, task):
        execution = TaskExecution(task.task_id)
        task.execution_history.append(execution)

        try:
            task.execute()
            task.status = TaskStatus.COMPLETED
            execution.status = ExecutionStatus.SUCCESS

        except Exception as error:
            task.status = TaskStatus.FAILED
            execution.status = ExecutionStatus.FAILED
            execution.error_message = str(error)

        finally:
            execution.completed_at = datetime.now()

    def stop(self):
        self.running=False

        if self.scheduler_thread:
            self.scheduler_thread.join()

        self.executor_worker.shutdown(wait=True)