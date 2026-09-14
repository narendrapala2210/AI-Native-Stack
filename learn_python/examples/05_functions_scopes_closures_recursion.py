"""
Python Concept Examples: 5. Functions, Scopes, Closures & Recursion
Documentation Reference: ../05.functions_scopes_closures_recursion.md
"""

import sys
import os

def example_1():
    """
    Example 1: Sliding-Window Rate Limiter via Closures
    """
    print("-" * 50)
    print("Running Example 1: Sliding-Window Rate Limiter via Closures")
    print("-" * 50)
    import time

    def create_rate_limiter(max_requests: int, window_seconds: float):
        timestamps = []

        def is_allowed() -> bool:
            nonlocal timestamps
            now = time.time()
            # Discard expired timestamps outside window
            timestamps = [t for t in timestamps if now - t < window_seconds]
            if len(timestamps) < max_requests:
                timestamps.append(now)
                return True
            return False

        return is_allowed

    limiter = create_rate_limiter(max_requests=2, window_seconds=0.1)

    print("Call 1 allowed?", limiter())  # True
    print("Call 2 allowed?", limiter())  # True
    print("Call 3 allowed?", limiter())  # False (Limit reached!)
    time.sleep(0.12)
    print("Call 4 allowed after delay?", limiter())  # True

def example_2():
    """
    Example 2: Functional Pipeline Composition Operator
    """
    print("-" * 50)
    print("Running Example 2: Functional Pipeline Composition Operator")
    print("-" * 50)
    from functools import reduce

    def compose(*functions):
        # Composes functions right-to-left: compose(f, g)(x) == f(g(x))
        return reduce(lambda f, g: lambda x: f(g(x)), functions, lambda x: x)

    def pipe(*functions):
        # Composes functions left-to-right: pipe(f, g)(x) == g(f(x))
        return reduce(lambda f, g: lambda x: g(f(x)), functions, lambda x: x)

    strip_whitespace = lambda s: s.strip()
    remove_dashes = lambda s: s.replace("-", "")
    to_uppercase = lambda s: s.upper()

    clean_serial_number = pipe(strip_whitespace, remove_dashes, to_uppercase)
    raw_input = "   sn-889-ab-01   "
    print("Cleaned serial:", clean_serial_number(raw_input))  # "SN889AB01"

def example_3():
    """
    Example 3: Nested Directory Tree Walker with Recursion Guard
    """
    print("-" * 50)
    print("Running Example 3: Nested Directory Tree Walker with Recursion Guard")
    print("-" * 50)
    file_system = {
        "root": {
            "src": {
                "app.py": "code",
                "utils": {
                    "helpers.py": "code"
                }
            },
            "README.md": "text"
        }
    }

    def walk_tree(node: dict, current_depth: int = 0, max_depth: int = 5):
        if current_depth > max_depth:
            print("  " * current_depth + "[!] Max recursion depth exceeded!")
            return

        for name, child in node.items():
            indent = "  " * current_depth
            if isinstance(child, dict):
                print(f"{indent}📁 {name}/")
                walk_tree(child, current_depth + 1, max_depth)
            else:
                print(f"{indent}📄 {name} ({child})")

    walk_tree(file_system)

if __name__ == "__main__":
    print("=" * 60)
    print("Executing 5. Functions, Scopes, Closures & Recursion Examples")
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
    print("Completed 5. Functions, Scopes, Closures & Recursion Examples")
    print("=" * 60)
