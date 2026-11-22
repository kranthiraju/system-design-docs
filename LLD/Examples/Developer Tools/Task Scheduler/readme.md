# Task Scheduler

A basic Python Task Scheduler that uses a **Min-Heap (`heapq`)** to schedule tasks and **ThreadPoolExecutor** to execute multiple tasks concurrently.

## Features

- Schedule one-time tasks with a specified delay.
- Maintain task execution order using a priority queue.
- Run the scheduler in a background thread.
- Execute multiple tasks concurrently using a configurable worker pool.
- Track task lifecycle and execution history.
- Cancel tasks before execution.
- Handle task execution failures.

## Example Usage

```python
import time
from task_scheduler import TaskScheduler, Task, TaskType

scheduler = TaskScheduler(max_workers=3)

task = Task(
    name="Example Task",
    action=lambda: print("Task executed"),
    task_type=TaskType.ONE_TIME,
    delay=2
)

scheduler.scheduleTask(task)
scheduler.start()

time.sleep(4)

print("Task Status:", task.status)

scheduler.stop()
```

## How It Works

1. **Task Scheduling:** `scheduleTask()` inserts tasks into a min-heap ordered by scheduled execution time.
2. **Task Dispatching:** The scheduler continuously checks whether the earliest task is ready for execution.
3. **Concurrent Execution:** Ready tasks are submitted to `ThreadPoolExecutor`.
4. **Worker Management:** The executor manages worker threads and executes tasks concurrently.
5. **Execution Tracking:** Each execution maintains its status, start time, completion time, and error details.
