"""
Python Concept Examples: 2. Built-in Data Types & Data Structures
Documentation Reference: ../02.builtin_data_types.md
"""

import sys
import os

def example_1():
    """
    Example 1: Financial Currency Ledger with Exact Precision
    """
    print("-" * 50)
    print("Running Example 1: Financial Currency Ledger with Exact Precision")
    print("-" * 50)
    from decimal import Decimal, ROUND_HALF_UP
    from fractions import Fraction

    class FinancialLedger:
        def __init__(self, tax_rate: str = "0.0825"):
            self.tax_rate = Decimal(tax_rate)
            self.entries = []

        def add_transaction(self, description: str, unit_price: str, quantity: int, split_fraction: tuple = (1, 1)):
            # Calculate split ratio exactly using Fraction
            ratio = Fraction(*split_fraction)
            unit = Decimal(unit_price)
            subtotal = (unit * quantity * Decimal(ratio.numerator)) / Decimal(ratio.denominator)
            tax = (subtotal * self.tax_rate).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
            total = subtotal + tax
            self.entries.append({"desc": description, "subtotal": subtotal, "tax": tax, "total": total})

        def print_summary(self):
            grand_total = sum(e["total"] for e in self.entries)
            for e in self.entries:
                print(f"Item: {e['desc']:<15} Subtotal: ${e['subtotal']:.2f} Tax: ${e['tax']:.2f} Total: ${e['total']:.2f}")
            print(f"Grand Total: ${grand_total:.2f}")

    ledger = FinancialLedger()
    ledger.add_transaction("Cloud Hosting", "149.99", 1, (1, 1))
    ledger.add_transaction("Shared DB Unit", "80.00", 1, (1, 2))  # 50% split
    ledger.print_summary()

def example_2():
    """
    Example 2: High-Performance Log Sanitizer with Unicode Normalization
    """
    print("-" * 50)
    print("Running Example 2: High-Performance Log Sanitizer with Unicode Normalization")
    print("-" * 50)
    import unicodedata
    import string

    class LogSanitizer:
        def __init__(self):
            # Strip control characters, punctuation, and map digits to '#'
            self.translation_table = str.maketrans(
                string.punctuation + string.digits,
                " " * len(string.punctuation) + "#" * len(string.digits)
            )

        def sanitize(self, raw_input: str) -> str:
            # 1. Normalize unicode (convert accents, symbols to canonical forms)
            normalized = unicodedata.normalize("NFKD", raw_input)
            # 2. Encode to ASCII bytes, ignoring non-ASCII artifacts, then decode
            ascii_clean = normalized.encode("ascii", "ignore").decode("utf-8")
            # 3. Translate symbols and mask numbers
            scrubbed = ascii_clean.translate(self.translation_table)
            # 4. Collapse extra whitespace
            return " ".join(scrubbed.split())

    sanitizer = LogSanitizer()
    dirty_log = "Alert! Usér: Alex-9921 failed login at IP: [192.168.1.105] (status: 404)!"
    print("Sanitized Output:", sanitizer.sanitize(dirty_log))

def example_3():
    """
    Example 3: Role-Based Access Control (RBAC) with `enum.Flag`
    """
    print("-" * 50)
    print("Running Example 3: Role-Based Access Control (RBAC) with `enum.Flag`")
    print("-" * 50)
    from enum import Flag, auto

    class UserPermission(Flag):
        NONE = 0
        VIEW_REPORTS = auto()     # 1
        EDIT_REPORTS = auto()     # 2
        DELETE_REPORTS = auto()   # 4
        MANAGE_USERS = auto()     # 8
        BILLING_ACCESS = auto()   # 16

        # Composite presets
        ANALYST = VIEW_REPORTS
        MANAGER = VIEW_REPORTS | EDIT_REPORTS | DELETE_REPORTS
        SUPERADMIN = VIEW_REPORTS | EDIT_REPORTS | DELETE_REPORTS | MANAGE_USERS | BILLING_ACCESS

    def authorize_action(user_role: UserPermission, required_perm: UserPermission) -> bool:
        return required_perm in user_role

    analyst_user = UserPermission.ANALYST
    manager_user = UserPermission.MANAGER

    print("Can analyst view reports?", authorize_action(analyst_user, UserPermission.VIEW_REPORTS))   # True
    print("Can analyst delete reports?", authorize_action(analyst_user, UserPermission.DELETE_REPORTS)) # False
    print("Can manager delete reports?", authorize_action(manager_user, UserPermission.DELETE_REPORTS)) # True

if __name__ == "__main__":
    print("=" * 60)
    print("Executing 2. Built-in Data Types & Data Structures Examples")
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
    print("Completed 2. Built-in Data Types & Data Structures Examples")
    print("=" * 60)
