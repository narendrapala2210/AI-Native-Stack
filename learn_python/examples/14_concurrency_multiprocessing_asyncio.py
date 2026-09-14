"""
Python Concept Examples: 14. Concurrency: Threading, Multiprocessing & AsyncIO
Documentation Reference: ../14.concurrency_multiprocessing_asyncio.md
"""

import sys
import os

def example_1():
    """
    Example 1: Concurrent Web Scraper / API Poller with `asyncio.TaskGroup`
    """
    print("-" * 50)
    print("Running Example 1: Concurrent Web Scraper / API Poller with `asyncio.TaskGroup`")
    print("-" * 50)
    import asyncio
    import time

    async def fetch_endpoint(url: str, delay: float) -> dict:
        await asyncio.sleep(delay)
        return {"url": url, "status": 200, "bytes": 1024}

    async def scrape_all():
        urls = [
            ("https://api.one/metrics", 0.05),
            ("https://api.two/users", 0.08),
            ("https://api.three/logs", 0.03)
        ]
        results = []
        async with asyncio.TaskGroup() as tg:
            tasks = [tg.create_task(fetch_endpoint(url, d)) for url, d in urls]

        for t in tasks:
            results.append(t.result())
        return results

    start = time.perf_counter()
    data = asyncio.run(scrape_all())
    elapsed = time.perf_counter() - start
    print(f"Fetched {len(data)} endpoints concurrently in {elapsed:.3f}s:")
    for item in data:
        print(f"  {item['url']} -> {item['status']}")

def example_2():
    """
    Example 2: Parallel Batch Matrix Compute Engine with `multiprocessing.Pool`
    """
    print("-" * 50)
    print("Running Example 2: Parallel Batch Matrix Compute Engine with `multiprocessing.Pool`")
    print("-" * 50)
    import multiprocessing
    import math

    def compute_heavy_factorials(number: int) -> int:
        return sum(math.factorial(i % 20) for i in range(number))

    if __name__ == "__main__":
        workloads = [200_000, 200_000, 200_000, 200_000]

        # Run across pool of workers
        with multiprocessing.Pool() as pool:
            outputs = pool.map(compute_heavy_factorials, workloads)
        print("Multi-core parallel computation results:", [o % 1000 for o in outputs])

def example_3():
    """
    Example 3: Multi-Threaded Producer-Consumer Pipeline with `queue.Queue`
    """
    print("-" * 50)
    print("Running Example 3: Multi-Threaded Producer-Consumer Pipeline with `queue.Queue`")
    print("-" * 50)
    import threading
    import time
    from queue import Queue

    task_queue = Queue()
    results = []

    def worker_consumer():
        while True:
            task = task_queue.get()
            if task is None:  # Shutdown sentinel
                task_queue.task_done()
                break
            # Process task
            time.sleep(0.01)
            results.append(f"Processed: {task}")
            task_queue.task_done()

    # Start 2 worker threads
    threads = [threading.Thread(target=worker_consumer) for _ in range(2)]
    for t in threads:
        t.start()

    # Produce 5 jobs
    for i in range(5):
        task_queue.put(f"Invoice-Job-{i+1}")

    # Wait for completion
    task_queue.join()

    # Stop workers
    for _ in threads:
        task_queue.put(None)
    for t in threads:
        t.join()

    print(f"Pipeline finished! Completed {len(results)} jobs.")

if __name__ == "__main__":
    print("=" * 60)
    print("Executing 14. Concurrency: Threading, Multiprocessing & AsyncIO Examples")
    print("=" * 60)

    try:
        example_1()
    except Exception as exc:
        print(f"Notice in Example 1: {exc}")
    print()
    try:
        example_2()
    except Exception as exc:
        print(f"Notice in Example 2: {exc}")
    print()
    try:
        example_3()
    except Exception as exc:
        print(f"Notice in Example 3: {exc}")
    print()
    print("=" * 60)
    print("Completed 14. Concurrency: Threading, Multiprocessing & AsyncIO Examples")
    print("=" * 60)
