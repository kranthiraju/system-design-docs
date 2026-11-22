import threading
import time
from worker_pool_management import WorkerPoolManagement, Job


manager = WorkerPoolManagement(max_workers=3)

def producer(producer_id):

    for i in range(5):

        job = Job(
            lambda: (
                print(f"Executing producer job {producer_id}"),
                time.sleep(1)
            )
        )

        print(f"Producer {producer_id} submitting job {i + 1}")
        manager.submit_job(job)


manager.start()

producers = []

for i in range(3):
    thread = threading.Thread(
        target=producer,
        args=(i + 1,)
    )

    producers.append(thread)
    thread.start()

for thread in producers:
    thread.join()

time.sleep(8)

manager.stop()