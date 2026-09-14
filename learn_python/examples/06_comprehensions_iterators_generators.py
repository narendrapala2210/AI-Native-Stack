"""
Python Concept Examples: 6. Comprehensions, Iterators & Generators
Documentation Reference: ../06.comprehensions_iterators_generators.md
"""

import sys
import os

def example_1():
    """
    Example 1: Memory-Efficient Large Log File Streaming
    """
    print("-" * 50)
    print("Running Example 1: Memory-Efficient Large Log File Streaming")
    print("-" * 50)
    import io

    def mock_log_source():
        logs = [
            "2026-09-14 10:00:00 [INFO] Server started",
            "2026-09-14 10:00:05 [ERROR] Connection refused to db_host:5432",
            "2026-09-14 10:00:10 [DEBUG] Health check OK",
            "2026-09-14 10:00:15 [ERROR] Out of memory in worker_thread_4"
        ]
        return io.StringIO("\n".join(logs))

    # Generator Pipeline
    def read_lines(stream):
        for line in stream:
            yield line.rstrip("\n")

    def filter_errors(lines):
        for line in lines:
            if "[ERROR]" in line:
                yield line

    def extract_message(error_lines):
        for line in error_lines:
            timestamp, _, msg = line.partition("[ERROR]")
            yield {"timestamp": timestamp.strip(), "message": msg.strip()}

    # Pipeline connects lazily:
    stream = mock_log_source()
    lines = read_lines(stream)
    errors = filter_errors(lines)
    parsed = extract_message(errors)

    for entry in parsed:
        print(f"CRITICAL LOG: {entry['timestamp']} -> {entry['message']}")

def example_2():
    """
    Example 2: Sliding Window Moving Average with `itertools.islice`
    """
    print("-" * 50)
    print("Running Example 2: Sliding Window Moving Average with `itertools.islice`")
    print("-" * 50)
    import itertools

    def rolling_window(iterable, window_size: int):
        # sliding window using tee and islice
        iterators = itertools.tee(iterable, window_size)
        for index, it in enumerate(iterators):
            for _ in range(index):
                next(it, None)  # Advance iterator
        return zip(*iterators)

    telemetry = [10.0, 12.0, 15.0, 18.0, 20.0, 25.0, 30.0]
    window = 3

    print(f"Rolling {window}-point moving averages:")
    for w in rolling_window(telemetry, window):
        avg = sum(w) / len(w)
        print(f"  Window {w} -> Moving Avg: {avg:.2f}")

def example_3():
    """
    Example 3: E-Commerce Category Cart Aggregator with `itertools.groupby`
    """
    print("-" * 50)
    print("Running Example 3: E-Commerce Category Cart Aggregator with `itertools.groupby`")
    print("-" * 50)
    import itertools
    from operator import itemgetter

    cart_items = [
        {"category": "Electronics", "name": "Mouse", "price": 45.0},
        {"category": "Books", "name": "Python Guide", "price": 30.0},
        {"category": "Electronics", "name": "Keyboard", "price": 95.0},
        {"category": "Books", "name": "System Design", "price": 50.0},
        {"category": "Apparel", "name": "Hoodie", "price": 60.0}
    ]

    # groupby requires the list to be sorted by the grouping key first!
    sorted_cart = sorted(cart_items, key=itemgetter("category"))

    print("Category Summaries:")
    for category, items in itertools.groupby(sorted_cart, key=itemgetter("category")):
        items_list = list(items)
        category_total = sum(i["price"] for i in items_list)
        print(f"  [{category}] {len(items_list)} items, Subtotal: ${category_total:.2f}")

if __name__ == "__main__":
    print("=" * 60)
    print("Executing 6. Comprehensions, Iterators & Generators Examples")
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
    print("Completed 6. Comprehensions, Iterators & Generators Examples")
    print("=" * 60)
