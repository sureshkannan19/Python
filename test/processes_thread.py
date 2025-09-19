import asyncio
import logging
import time
import threading
import multiprocessing

class TaskIdFilter(logging.Filter):
    def filter(self, record):
        try:
            task = asyncio.current_task()
            record.task_id = id(task) if task else "N/A"
        except RuntimeError:
            # No running event loop (e.g., sync function in threadpool)
            record.task_id = "N/A"

        return True

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s.%(msecs)03d [Thread:%(thread)d] [Task:%(task_id)s] [%(levelname)s] %(name)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

logging.getLogger().addFilter(TaskIdFilter())

# CPU-bound function: waste time doing math
def cpu_task(n: int,task : str):
    logging.info(f"Task started by {task}")
    count = 0
    for i in range(n):
        count += i*i
    logging.info(f"Task ended by {task}")
    return count

# Wrapper to measure time with threads
def run_threads(n_tasks, n):
    threads = []
    start = time.time()
    for _ in range(n_tasks):
        t = threading.Thread(target=cpu_task, args=(n,"Thread"))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    end = time.time()
    return end - start

# Wrapper to measure time with processes
def run_processes(n_tasks, n):
    processes = []
    start = time.time()
    for _ in range(n_tasks):
        p = multiprocessing.Process(target=cpu_task, args=(n,"Process"))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()
    end = time.time()
    return end - start


if __name__ == "__main__":
    N = 100_000_000
    print("Running threads...")
    print("Time:", run_threads(2, N))

    print("Running processes...")
    print("Time:", run_processes(2, N))
