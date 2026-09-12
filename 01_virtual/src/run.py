"""Display details about the Python environment running this lesson."""

import platform
import sys


def main() -> None:
    """Print interpreter details useful for checking virtual environment setup."""
    print("=" * 50)
    print(" PYTHON ENVIRONMENT DIAGNOSTIC ")
    print("=" * 50)
    print(f"Python version     : {platform.python_version()}")
    print(f"Python executable  : {sys.executable}")
    print(f"Environment prefix : {sys.prefix}")
    print(f"Base Python prefix : {sys.base_prefix}")

    is_venv = sys.prefix != sys.base_prefix
    status = "ACTIVE (.venv)" if is_venv else "NOT ACTIVE (Global / System Python)"
    print(f"Virtual environment: {status}")
    print("=" * 50)


if __name__ == "__main__":
    main()
