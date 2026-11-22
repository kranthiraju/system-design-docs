import time
from task_scheduler import TaskScheduler, Task, TaskType

task_scheduler = TaskScheduler()
task_scheduler.start()


task1 = Task("Task 1", lambda: (time.sleep(5), print("======== Task1 executed ========")), TaskType.ONE_TIME, delay=5)
task_scheduler.scheduleTask(task1)

# time.sleep(2)
task2 = Task("Task 2", lambda: (time.sleep(2), print("======== Task2 executed ========")), TaskType.ONE_TIME, delay=5)
task_scheduler.scheduleTask(task2)

task3 = Task("Task 3", lambda: print("======== Task3 executed ========"), TaskType.ONE_TIME, delay=5)
task_scheduler.scheduleTask(task3)

task4 = Task("Task 4", lambda: (time.sleep(2), print("======== Task4 executed ========")), TaskType.ONE_TIME, delay=5)
task_scheduler.scheduleTask(task4)


for _ in range(15):
    print("Task1 Status: ", task1.status)
    print("Task2 Status: ", task2.status)
    print("Task3 Status: ", task3.status)
    print("Task4 Status: ", task4.status)
    print("\n\n")
    time.sleep(1)

# print(task1.execution_history[0].__str__())

task_scheduler.stop()
