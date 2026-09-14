"""
Python Concept Examples: 10. Robust Exception & Error Handling
Documentation Reference: ../10.exception_and_error_handling.md
"""

import sys
import os

def example_1():
    """
    Example 1: Transactional Atomic File Writer Context Manager
    """
    print("-" * 50)
    print("Running Example 1: Transactional Atomic File Writer Context Manager")
    print("-" * 50)
    import os
    import contextlib
    from pathlib import Path

    @contextlib.contextmanager
    def atomic_file_writer(file_path: Path):
        temp_path = file_path.with_suffix(file_path.suffix + ".tmp")
        try:
            with open(temp_path, "w", encoding="utf-8") as f:
                yield f  # Allow client to write to temp file
            # Replace atomically only if no exceptions were raised
            temp_path.replace(file_path)
            print(f"[ATOMIC WRITE] Successfully committed to {file_path}")
        except Exception as e:
            if temp_path.exists():
                temp_path.unlink()  # Rollback changes by deleting temp file
            print(f"[ATOMIC WRITE ROLLBACK] Write failed due to: {e}. Original file preserved.")
            raise

    target = Path("config.json")
    try:
        with atomic_file_writer(target) as f:
            f.write('{"status": "OK", "version": 1}')
        print("Content:", target.read_text())

        # Test failure rollback
        with atomic_file_writer(target) as f:
            f.write('{"corrupted": true}')
            raise RuntimeError("Disk write failed midway!")
    except RuntimeError:
        pass

    print("Content after failed write:", target.read_text())  # Still untouched!
    target.unlink(missing_ok=True)

def example_2():
    """
    Example 2: Multi-Service Health Checker with `ExceptionGroup` (Python 3.11+)
    """
    print("-" * 50)
    print("Running Example 2: Multi-Service Health Checker with `ExceptionGroup` (Python 3.11+)")
    print("-" * 50)
    def check_database():
        raise ConnectionError("Database cluster unreachable")

    def check_cache():
        raise TimeoutError("Redis cache timed out")

    def check_auth_token():
        raise PermissionError("Auth secret expired")

    def run_health_checks():
        failures = []
        checks = [check_database, check_cache, check_auth_token]
        for check in checks:
            try:
                check()
            except Exception as err:
                failures.append(err)
        if failures:
            raise ExceptionGroup("Multiple system health checks failed", failures)

    try:
        run_health_checks()
    except* ConnectionError as eg_conn:
        print("[HANDLED CONNECTION ERROR]", eg_conn.exceptions)
    except* TimeoutError as eg_time:
        print("[HANDLED TIMEOUT ERROR]", eg_time.exceptions)
    except* PermissionError as eg_perm:
        print("[HANDLED AUTH ERROR]", eg_perm.exceptions)

def example_3():
    """
    Example 3: Banking Security Shield with Explicit Chaining
    """
    print("-" * 50)
    print("Running Example 3: Banking Security Shield with Explicit Chaining")
    print("-" * 50)
    class BankingServiceError(Exception):
        # Domain-level exception
        pass

    class DatabaseDriverError(Exception):
        # Internal driver error
        pass

    def execute_sql_transfer(amount):
        raise DatabaseDriverError("Deadlock detected in row 409")

    def transfer_funds(from_acc: str, to_acc: str, amount: float):
        try:
            execute_sql_transfer(amount)
        except DatabaseDriverError as db_err:
            # Explicitly chain with 'from' to preserve underlying cause
            raise BankingServiceError(f"Failed to transfer ${amount:.2f} from {from_acc} to {to_acc}") from db_err

    try:
        transfer_funds("ACC-1", "ACC-2", 500.0)
    except BankingServiceError as bse:
        print(f"[SHIELDED ERROR]: {bse}")
        print(f"  Underlying cause was: {bse.__cause__}")

if __name__ == "__main__":
    print("=" * 60)
    print("Executing 10. Robust Exception & Error Handling Examples")
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
    print("Completed 10. Robust Exception & Error Handling Examples")
    print("=" * 60)
