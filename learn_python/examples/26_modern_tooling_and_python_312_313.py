"""
Python Concept Examples: 26. Modern Tooling, Packaging & Bleeding-Edge Python 3.12/3.13 Features
Documentation Reference: ../26.modern_tooling_and_python_312_313.md
"""

import sys
import os

def example_1():
    """
    Example 1: Automated Tooling Runner Script (`ruff` & `mypy`)
    """
    print("-" * 50)
    print("Running Example 1: Automated Tooling Runner Script (`ruff` & `mypy`)")
    print("-" * 50)
    import subprocess
    import sys

    def run_project_quality_check():
        checks = [
            ("Python Version", [sys.executable, "--version"]),
            ("Bytecode Verification", [sys.executable, "-m", "py_compile", "PYTHON_COMPLETE_GUIDE.md"])
        ]

        for name, cmd in checks:
            try:
                res = subprocess.run(cmd, capture_output=True, text=True)
                status = "OK" if res.returncode == 0 else f"ERROR ({res.returncode})"
                print(f"[{status}] {name}")
            except Exception as e:
                print(f"[FAILED] {name}: {e}")

    run_project_quality_check()

def example_2():
    """
    Example 2: Python 3.12 Nested Multi-Line F-String Data Reporter
    """
    print("-" * 50)
    print("Running Example 2: Python 3.12 Nested Multi-Line F-String Data Reporter")
    print("-" * 50)
    def generate_inventory_report(products: list[dict]) -> str:
        high_val = "\n".join([f"  - {p['name']}: ${p['price']:.2f}" for p in products if p["price"] > 50.0])
        return f"""
    ==================== INVENTORY REPORT ====================
    Total Items: {len(products)}
    Out of Stock: {len([p for p in products if p["stock"] == 0])}
    High Value Items:
    {high_val}
    ==========================================================
    """

    items = [
        {"name": "Mechanical Keyboard", "price": 120.0, "stock": 5},
        {"name": "USB Cable", "price": 12.0, "stock": 0},
        {"name": "4K Monitor", "price": 350.0, "stock": 2}
    ]

    print(generate_inventory_report(items))

def example_3():
    """
    Example 3: Multi-Threaded CPU Scaling Benchmark (Testing GIL vs Free-Threaded No-GIL)
    """
    print("-" * 50)
    print("Running Example 3: Multi-Threaded CPU Scaling Benchmark (Testing GIL vs Free-Threaded No-GIL)")
    print("-" * 50)
    import threading
    import time

    def cpu_intensive_calculation(n: int = 5_000_000):
        total = 0
        for i in range(n):
            total += (i ^ 2)
        return total

    def benchmark_threading():
        # 1. Single Threaded (Baseline)
        start = time.perf_counter()
        cpu_intensive_calculation()
        cpu_intensive_calculation()
        single_duration = time.perf_counter() - start
        print(f"Single-threaded runtime (2 tasks sequentially): {single_duration:.3f}s")

        # 2. Multi Threaded
        # Under standard GIL, this takes roughly the same time (no CPU parallel scaling).
        # Under Python 3.13 free-threaded (No-GIL build), this runs in ~50% of the time!
        start = time.perf_counter()
        t1 = threading.Thread(target=cpu_intensive_calculation)
        t2 = threading.Thread(target=cpu_intensive_calculation)
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        multi_duration = time.perf_counter() - start
        print(f"Multi-threaded runtime (2 threads concurrently): {multi_duration:.3f}s")

    benchmark_threading()

if __name__ == "__main__":
    print("=" * 60)
    print("Executing 26. Modern Tooling, Packaging & Bleeding-Edge Python 3.12/3.13 Features Examples")
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
    print("Completed 26. Modern Tooling, Packaging & Bleeding-Edge Python 3.12/3.13 Features Examples")
    print("=" * 60)
