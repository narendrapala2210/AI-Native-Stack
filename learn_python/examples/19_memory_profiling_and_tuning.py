"""
Python Concept Examples: 19. Memory Profiling, Optimization & Performance Tuning
Documentation Reference: ../19.memory_profiling_and_tuning.md
"""

import sys
import os

def example_1():
    """
    Example 1: Memory Leak Detection with `tracemalloc` Line Tracking
    """
    print("-" * 50)
    print("Running Example 1: Memory Leak Detection with `tracemalloc` Line Tracking")
    print("-" * 50)
    import tracemalloc

    def simulate_leaky_operation():
        cache = []
        for i in range(25_000):
            cache.append(f"Cached string allocation #{i} with padding data...")
        return cache

    tracemalloc.start()
    baseline = tracemalloc.take_snapshot()

    # Run potentially leaky function
    leaked_data = simulate_leaky_operation()

    current = tracemalloc.take_snapshot()
    stats_diff = current.compare_to(baseline, "lineno")

    print("Top 3 Memory Allocators (Delta):")
    for stat in stats_diff[:3]:
        print(f"  {stat}")

    tracemalloc.stop()

def example_2():
    """
    Example 2: Profiling Slow Calculations with `cProfile` and `pstats`
    """
    print("-" * 50)
    print("Running Example 2: Profiling Slow Calculations with `cProfile` and `pstats`")
    print("-" * 50)
    import cProfile
    import pstats
    import io

    def heavy_computation():
        return sum(x ** 2 for x in range(150_000))

    def light_computation():
        return [x for x in range(10_000)]

    def run_app():
        heavy_computation()
        light_computation()

    profiler = cProfile.Profile()
    profiler.enable()
    run_app()
    profiler.disable()

    stream = io.StringIO()
    stats = pstats.Stats(profiler, stream=stream).sort_stats("cumulative")
    stats.print_stats(3)
    print("Profile Summary (Top 3 slowest calls):", stream.getvalue()[:350])

def example_3():
    """
    Example 3: Auto-Clearing Ephemeral Object Cache with `weakref.WeakValueDictionary`
    """
    print("-" * 50)
    print("Running Example 3: Auto-Clearing Ephemeral Object Cache with `weakref.WeakValueDictionary`")
    print("-" * 50)
    import weakref

    class HeavySessionModel:
        def __init__(self, session_id: str):
            self.session_id = session_id

    session_cache = weakref.WeakValueDictionary()

    # Active session
    session_1 = HeavySessionModel("sess_101")
    session_cache["active_user"] = session_1

    print("Found in cache:", session_cache.get("active_user").session_id)

    # User logs out or closes browser -> strong reference deleted
    del session_1

    # WeakValueDictionary automatically discards the key!
    print("Found in cache after logout?", session_cache.get("active_user"))  # None

if __name__ == "__main__":
    print("=" * 60)
    print("Executing 19. Memory Profiling, Optimization & Performance Tuning Examples")
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
    print("Completed 19. Memory Profiling, Optimization & Performance Tuning Examples")
    print("=" * 60)
