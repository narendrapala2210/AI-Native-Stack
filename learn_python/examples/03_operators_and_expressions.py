"""
Python Concept Examples: 3. Operators & Expressions
Documentation Reference: ../03.operators_and_expressions.md
"""

import sys
import os

def example_1():
    """
    Example 1: Stream Processing with the Walrus Operator (`:=`)
    """
    print("-" * 50)
    print("Running Example 1: Stream Processing with the Walrus Operator (`:=`)")
    print("-" * 50)
    import io

    def mock_data_stream():
        return io.StringIO("alpha:100\nbeta:200\n\ngamma:300\nSTOP\ndelta:400\n")

    stream = mock_data_stream()
    records = []

    # Walrus assignment expressions inside loop conditional
    while (line := stream.readline()) and (trimmed := line.strip()) != "STOP":
        if trimmed and ":" in trimmed:
            key, val = trimmed.split(":")
            records.append({key: int(val)})

    print("Stream ingested records:", records)

def example_2():
    """
    Example 2: Bitmask Feature Flag Configuration Engine
    """
    print("-" * 50)
    print("Running Example 2: Bitmask Feature Flag Configuration Engine")
    print("-" * 50)
    class FeatureFlagManager:
        FEATURE_DARK_MODE    = 1 << 0  # 1
        FEATURE_AI_ASSISTANT = 1 << 1  # 2
        FEATURE_BETA_TESTING = 1 << 2  # 4
        FEATURE_SSO_LOGIN    = 1 << 3  # 8

        def __init__(self, initial_flags: int = 0):
            self.flags = initial_flags

        def enable(self, feature: int):
            self.flags |= feature

        def disable(self, feature: int):
            self.flags &= ~feature

        def is_enabled(self, feature: int) -> bool:
            return bool(self.flags & feature)

    mgr = FeatureFlagManager()
    mgr.enable(FeatureFlagManager.FEATURE_DARK_MODE | FeatureFlagManager.FEATURE_AI_ASSISTANT)

    print("Dark Mode on?", mgr.is_enabled(FeatureFlagManager.FEATURE_DARK_MODE))         # True
    print("Beta Testing on?", mgr.is_enabled(FeatureFlagManager.FEATURE_BETA_TESTING))   # False

    mgr.disable(FeatureFlagManager.FEATURE_DARK_MODE)
    print("Dark Mode after disable:", mgr.is_enabled(FeatureFlagManager.FEATURE_DARK_MODE)) # False

def example_3():
    """
    Example 3: Safe Arithmetic Calculator with Operator Mapping
    """
    print("-" * 50)
    print("Running Example 3: Safe Arithmetic Calculator with Operator Mapping")
    print("-" * 50)
    import operator

    OPERATORS = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
        "//": operator.floordiv,
        "%": operator.mod,
        "**": operator.pow,
    }

    def safe_calculate(num1: float, op_str: str, num2: float) -> float:
        if op_str not in OPERATORS:
            raise ValueError(f"Unsupported math operator: '{op_str}'")
        if op_str in ("/", "//", "%") and num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero!")
        return OPERATORS[op_str](num1, num2)

    print("15 * 4 =", safe_calculate(15, "*", 4))
    print("2 ** 8 =", safe_calculate(2, "**", 8))
    print("17 // 3 =", safe_calculate(17, "//", 3))

if __name__ == "__main__":
    print("=" * 60)
    print("Executing 3. Operators & Expressions Examples")
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
    print("Completed 3. Operators & Expressions Examples")
    print("=" * 60)
