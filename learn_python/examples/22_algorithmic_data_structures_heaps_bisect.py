"""
Python Concept Examples: 22. Algorithmic Data Structures: Heaps, Bisect & Performance Extractors
Documentation Reference: ../22.algorithmic_data_structures_heaps_bisect.md
"""

import sys
import os

def example_1():
    """
    Example 1: Priority Job Scheduler with Task Preemption via `heapq`
    """
    print("-" * 50)
    print("Running Example 1: Priority Job Scheduler with Task Preemption via `heapq`")
    print("-" * 50)
    import heapq
    import time

    class PriorityScheduler:
        def __init__(self):
            self._queue = []
            self._index = 0

        def add_job(self, name: str, priority: int):
            # Priority: lower integer = higher priority
            # index avoids comparison collision on duplicate priorities
            heapq.heappush(self._queue, (priority, self._index, name))
            self._index += 1

        def pop_next_job(self) -> str | None:
            if not self._queue:
                return None
            priority, _, name = heapq.heappop(self._queue)
            return f"Job: {name} (Priority {priority})"

    scheduler = PriorityScheduler()
    scheduler.add_job("Batch log upload", priority=3)
    scheduler.add_job("Emergency failover", priority=1)
    scheduler.add_job("Send marketing emails", priority=2)

    while job := scheduler.pop_next_job():
        print("Executing:", job)

def example_2():
    """
    Example 2: Dynamic Leaderboard with Fast Insertion via `bisect`
    """
    print("-" * 50)
    print("Running Example 2: Dynamic Leaderboard with Fast Insertion via `bisect`")
    print("-" * 50)
    import bisect

    class SortedLeaderboard:
        def __init__(self):
            self.scores = []  # Kept sorted ascending

        def add_score(self, score: int):
            bisect.insort(self.scores, score)

        def get_rank(self, score: int) -> int:
            # How many players scored strictly lower?
            lower_count = bisect.bisect_left(self.scores, score)
            return len(self.scores) - lower_count  # 1-based rank

    board = SortedLeaderboard()
    for s in [100, 250, 400, 150, 300]:
        board.add_score(s)

    print("Current sorted scores:", board.scores)
    print("Rank of 250:", board.get_rank(250))
    print("Rank of 500 (New high score!):", board.get_rank(500))

def example_3():
    """
    Example 3: High-Performance Multi-Field Record Sorter with `operator.itemgetter`
    """
    print("-" * 50)
    print("Running Example 3: High-Performance Multi-Field Record Sorter with `operator.itemgetter`")
    print("-" * 50)
    from operator import itemgetter

    records = [
        {"dept": "Engineering", "level": 3, "name": "Charlie"},
        {"dept": "Sales", "level": 2, "name": "Alice"},
        {"dept": "Engineering", "level": 5, "name": "Bob"},
        {"dept": "Sales", "level": 4, "name": "Diana"}
    ]

    # Sort by department ASCENDING, then level DESCENDING
    # To invert numeric sorts, sort in passes:
    records.sort(key=itemgetter("level"), reverse=True)
    records.sort(key=itemgetter("dept"))

    print("Sorted Records:")
    for r in records:
        print(f"  {r['dept']:<12} Level {r['level']} - {r['name']}")

if __name__ == "__main__":
    print("=" * 60)
    print("Executing 22. Algorithmic Data Structures: Heaps, Bisect & Performance Extractors Examples")
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
    print("Completed 22. Algorithmic Data Structures: Heaps, Bisect & Performance Extractors Examples")
    print("=" * 60)
