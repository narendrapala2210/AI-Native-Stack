"""
Python Concept Examples: 18. Testing & Mocking Mastery
Documentation Reference: ../18.testing_and_mocking_mastery.md
"""

import sys
import os

def example_1():
    """
    Example 1: Mocking Third-Party HTTP APIs with `@patch` and `MagicMock`
    """
    print("-" * 50)
    print("Running Example 1: Mocking Third-Party HTTP APIs with `@patch` and `MagicMock`")
    print("-" * 50)
    from unittest.mock import patch, MagicMock
    import unittest

    class PaymentGatewayClient:
        def charge_card(self, token: str, amount: float) -> dict:
            import urllib.request
            # Simulated external HTTP request
            return {"status": "SUCCESS", "id": "tx_9988"}

    def process_order(client: PaymentGatewayClient, token: str, amount: float) -> bool:
        res = client.charge_card(token, amount)
        return res.get("status") == "SUCCESS"

    class TestOrderPayment(unittest.TestCase):
        @patch.object(PaymentGatewayClient, "charge_card")
        def test_successful_charge(self, mock_charge):
            mock_charge.return_value = {"status": "SUCCESS", "id": "tx_fake_001"}

            client = PaymentGatewayClient()
            success = process_order(client, "tok_visa", 49.99)

            self.assertTrue(success)
            mock_charge.assert_called_once_with("tok_visa", 49.99)
            print("Mock test passed successfully!")

    suite = unittest.TestLoader().loadTestsFromTestCase(TestOrderPayment)
    unittest.TextTestRunner(verbosity=2).run(suite)

def example_2():
    """
    Example 2: Data-Driven Parametrized Input Testing (pytest pattern)
    """
    print("-" * 50)
    print("Running Example 2: Data-Driven Parametrized Input Testing (pytest pattern)")
    print("-" * 50)
    def validate_password_strength(password: str) -> bool:
        # Requires at least 8 chars, 1 digit, 1 uppercase
        if len(password) < 8:
            return False
        if not any(c.isdigit() for c in password):
            return False
        if not any(c.isupper() for c in password):
            return False
        return True

    # Parametrized test runner
    test_cases = [
        ("short", False),
        ("NoDigitsHere", False),
        ("alllowercase123", False),
        ("ValidPass123", True),
        ("SuperSecure2026!", True)
    ]

    for pwd, expected in test_cases:
        result = validate_password_strength(pwd)
        assert result == expected, f"Failed on '{pwd}': expected {expected}, got {result}"
        print(f"PASS: '{pwd}' -> {result}")

def example_3():
    """
    Example 3: Self-Testing String Normalizer with `doctest`
    """
    print("-" * 50)
    print("Running Example 3: Self-Testing String Normalizer with `doctest`")
    print("-" * 50)
    import doctest

    def sanitize_slug(text: str) -> str:
        r"""
        Convert raw titles into URL-safe slugs.

        >>> sanitize_slug("Hello World!")
        'hello-world'
        >>> sanitize_slug("  Python 3.12 Deep Dive  ")
        'python-312-deep-dive'
        >>> sanitize_slug("AI & Machine Learning")
        'ai-machine-learning'
        """
        clean = "".join(c.lower() if c.isalnum() or c.isspace() else "" for c in text)
        return "-".join(clean.split())

    res = doctest.testmod()
    print(f"Doctest finished: {res.attempted} tests run, {res.failed} failures.")

if __name__ == "__main__":
    print("=" * 60)
    print("Executing 18. Testing & Mocking Mastery Examples")
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
    print("Completed 18. Testing & Mocking Mastery Examples")
    print("=" * 60)
