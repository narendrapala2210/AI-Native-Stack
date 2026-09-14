"""
Python Concept Examples: 16. Python CLI Flags, Runtime Options & Environment Variables
Documentation Reference: ../16.python_cli_flags_and_env_vars.md
"""

import sys
import os

def example_1():
    """
    Example 1: Multi-Environment App Configuration Loader (Dev/Staging/Prod)
    """
    print("-" * 50)
    print("Running Example 1: Multi-Environment App Configuration Loader (Dev/Staging/Prod)")
    print("-" * 50)
    import os

    class EnvironmentConfig:
        def __init__(self):
            self.env = os.getenv("APP_ENV", "development").lower()
            self.debug = os.getenv("DEBUG", "true").lower() in ("1", "true", "yes")
            self.port = int(os.getenv("PORT", "8000"))

        def print_config(self):
            print(f"Loaded Environment: {self.env.upper()}")
            print(f"Debug Mode:        {self.debug}")
            print(f"Listening Port:    {self.port}")

    # Test with temporary env var override
    os.environ["APP_ENV"] = "production"
    os.environ["DEBUG"] = "false"
    os.environ["PORT"] = "443"

    config = EnvironmentConfig()
    config.print_config()

def example_2():
    """
    Example 2: Runtime Optimization & Assertions Checker (`-O` Flag)
    """
    print("-" * 50)
    print("Running Example 2: Runtime Optimization & Assertions Checker (`-O` Flag)")
    print("-" * 50)
    # Run this script with:
    #   python script.py       -> Debug mode active, assertions enforced
    #   python -O script.py    -> Optimized mode, assertions stripped!

    def process_secure_transaction(amount: float):
        # This assert is completely stripped out when -O is passed!
        assert amount > 0, "Amount must be strictly positive!"
        return f"Processed: ${amount:.2f}"

    print("Is Python running in debug mode?", __debug__)
    try:
        print(process_secure_transaction(50.0))
    except AssertionError as ae:
        print("[ASSERTION FAILED]", ae)

def example_3():
    """
    Example 3: Unbuffered Output Demonstration (Simulating `-u` Flag)
    """
    print("-" * 50)
    print("Running Example 3: Unbuffered Output Demonstration (Simulating `-u` Flag)")
    print("-" * 50)
    import sys
    import time

    def stream_logs(unbuffered: bool = False):
        print(f"Streaming logs (Unbuffered={unbuffered}):")
        for i in range(3):
            # With flush=True or -u flag, output appears immediately in Docker / Kubernetes logs
            print(f"Heartbeat #{i}", end=" ", flush=unbuffered)
            time.sleep(0.02)
        print("\nDone.")

    stream_logs(unbuffered=True)

if __name__ == "__main__":
    print("=" * 60)
    print("Executing 16. Python CLI Flags, Runtime Options & Environment Variables Examples")
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
    print("Completed 16. Python CLI Flags, Runtime Options & Environment Variables Examples")
    print("=" * 60)
