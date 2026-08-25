"""Display details about the Python environment running this lesson."""

import platform
import sys


def main() -> None:
	"""Print interpreter details useful for checking virtual-environment setup."""
	print(f"Python version: {platform.python_version()}")
	print(f"Python executable: {sys.executable}")
	print(f"Environment prefix: {sys.prefix}")
	print(f"Base Python prefix: {sys.base_prefix}")

	if sys.prefix != sys.base_prefix:
		print("Virtual environment: active")
	else:
		print("Virtual environment: not active")


if __name__ == "__main__":
	main()
