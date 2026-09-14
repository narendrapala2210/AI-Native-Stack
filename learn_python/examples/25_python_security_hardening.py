"""
Python Concept Examples: 25. Python Security Hardening & Vulnerability Mitigation
Documentation Reference: ../25.python_security_hardening.md
"""

import sys
import os

def example_1():
    """
    Example 1: SQL Injection Vulnerability Exploit & Parameterized Defense
    """
    print("-" * 50)
    print("Running Example 1: SQL Injection Vulnerability Exploit & Parameterized Defense")
    print("-" * 50)
    import sqlite3

    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE accounts (username TEXT, balance INT)")
    conn.execute("INSERT INTO accounts VALUES ('alice', 1000), ('admin', 50000)")
    conn.commit()

    # Malicious user input
    evil_input = "alice' OR 1=1; --"

    # VULNERABLE WAY: string concatenation
    vuln_sql = f"SELECT * FROM accounts WHERE username = '{evil_input}'"
    print("Vulnerable SQL Query:", vuln_sql)
    leaked = conn.execute(vuln_sql).fetchall()
    print("VULNERABILITY: Attacker retrieved all accounts:", leaked)

    # SECURE WAY: parameterized query
    secure_sql = "SELECT * FROM accounts WHERE username = ?"
    safe_results = conn.execute(secure_sql, (evil_input,)).fetchall()
    print("SECURE RESULT: Injection harmlessly treated as literal string:", safe_results)

def example_2():
    """
    Example 2: Path Traversal Defense with `pathlib.Path.is_relative_to`
    """
    print("-" * 50)
    print("Running Example 2: Path Traversal Defense with `pathlib.Path.is_relative_to`")
    print("-" * 50)
    from pathlib import Path
    import tempfile

    with tempfile.TemporaryDirectory() as base_tmp:
        ALLOWED_STORAGE = Path(base_tmp).resolve()

        # Create safe file
        (ALLOWED_STORAGE / "user_doc.txt").write_text("Safe internal file content.")

        def secure_read_file(user_filename: str) -> str:
            # Resolve path to canonical absolute path
            requested_path = (ALLOWED_STORAGE / user_filename).resolve()

            # Guard: Check containment
            if not requested_path.is_relative_to(ALLOWED_STORAGE):
                raise PermissionError(f"Directory traversal attack detected: '{user_filename}'")

            return requested_path.read_text()

        print("Safe read output:", secure_read_file("user_doc.txt"))
        try:
            secure_read_file("../../Windows/System32/drivers/etc/hosts")
        except PermissionError as pe:
            print("SECURITY BLOCKED:", pe)

def example_3():
    """
    Example 3: Constant-Time Token Comparison Preventing Timing Attacks
    """
    print("-" * 50)
    print("Running Example 3: Constant-Time Token Comparison Preventing Timing Attacks")
    print("-" * 50)
    import hmac
    import time

    def verify_token_constant_time(provided_token: str, real_token: str) -> bool:
        # hmac.compare_digest avoids early return on first mismatch character,
        # preventing attackers from inferring key characters by measuring nanosecond timing!
        return hmac.compare_digest(provided_token.encode("utf-8"), real_token.encode("utf-8"))

    stored_key = "secret_auth_token_992211"
    attempt_1 = "secret_auth_token_992211"
    attempt_2 = "secret_auth_token_000000"

    print("Valid token match:", verify_token_constant_time(attempt_1, stored_key))  # True
    print("Invalid token match:", verify_token_constant_time(attempt_2, stored_key)) # False

if __name__ == "__main__":
    print("=" * 60)
    print("Executing 25. Python Security Hardening & Vulnerability Mitigation Examples")
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
    print("Completed 25. Python Security Hardening & Vulnerability Mitigation Examples")
    print("=" * 60)
