"""
Python Concept Examples: 20. AI & Data Science Python Foundations
Documentation Reference: ../20.ai_and_data_science_foundations.md
"""

import sys
import os

def example_1():
    """
    Example 1: SIMD Vectorization vs Python Loop Benchmark
    """
    print("-" * 50)
    print("Running Example 1: SIMD Vectorization vs Python Loop Benchmark")
    print("-" * 50)
    import time

    def benchmark_loops():
        size = 500_000
        a = list(range(size))
        b = list(range(size))

        start = time.perf_counter()
        # Pure Python loop: pointer chasing on each iteration
        result = [x * 2 + y for x, y in zip(a, b)]
        duration = time.perf_counter() - start

        print(f"Python list comprehension ({size:,} items): {duration:.4f} seconds")
        print(f"First 3 elements: {result[:3]}")

    benchmark_loops()

def example_2():
    """
    Example 2: Columnar Data Processing and Filtering Engine
    """
    print("-" * 50)
    print("Running Example 2: Columnar Data Processing and Filtering Engine")
    print("-" * 50)
    class ColumnarTable:
        def __init__(self, columns: dict[str, list]):
            self.columns = columns
            self.row_count = len(next(iter(columns.values())))

        def filter_gt(self, column: str, threshold: float) -> dict[str, list]:
            indices = [i for i, val in enumerate(self.columns[column]) if val > threshold]
            return {col: [self.columns[col][i] for i in indices] for col in self.columns}

    data = ColumnarTable({
        "id": [1, 2, 3, 4, 5],
        "model_score": [0.85, 0.94, 0.72, 0.99, 0.65],
        "is_active": [True, True, False, True, False]
    })

    high_scoring = data.filter_gt("model_score", 0.90)
    print("High scoring predictions (Vectorized filter):", high_scoring)

def example_3():
    """
    Example 3: Secure Environment Secret Masker & Validator
    """
    print("-" * 50)
    print("Running Example 3: Secure Environment Secret Masker & Validator")
    print("-" * 50)
    import os

    def get_masked_secret(env_var_name: str, min_length: int = 10) -> str:
        val = os.getenv(env_var_name, "sk-mock-demo-key-123456789")
        if len(val) < min_length:
            raise ValueError(f"Environment variable '{env_var_name}' appears malformed or too short.")
        # Mask middle characters
        masked = f"{val[:3]}...{val[-4:]}"
        return masked

    print("Masked Secret for Logging:", get_masked_secret("OPENAI_API_KEY"))

if __name__ == "__main__":
    print("=" * 60)
    print("Executing 20. AI & Data Science Python Foundations Examples")
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
    print("Completed 20. AI & Data Science Python Foundations Examples")
    print("=" * 60)
