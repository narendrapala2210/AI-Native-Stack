"""
Python Concept Examples: 9. Metaprogramming, Descriptors & Dynamic Python
Documentation Reference: ../09.metaprogramming_and_descriptors.md
"""

import sys
import os

def example_1():
    """
    Example 1: Production ORM Field Validator with Descriptor Protocol
    """
    print("-" * 50)
    print("Running Example 1: Production ORM Field Validator with Descriptor Protocol")
    print("-" * 50)
    class StringField:
        def __set_name__(self, owner, name):
            self.public_name = name
            self.private_name = f"_{name}"

        def __get__(self, instance, owner):
            if instance is None:
                return self
            return getattr(instance, self.private_name, "")

        def __set__(self, instance, value):
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f"Field '{self.public_name}' must be a non-empty string.")
            setattr(instance, self.private_name, value.strip())

    class IntegerField:
        def __init__(self, min_val: int = 0, max_val: int = 150):
            self.min_val = min_val
            self.max_val = max_val

        def __set_name__(self, owner, name):
            self.public_name = name
            self.private_name = f"_{name}"

        def __get__(self, instance, owner):
            if instance is None:
                return self
            return getattr(instance, self.private_name, 0)

        def __set__(self, instance, value):
            if not isinstance(value, int) or not (self.min_val <= value <= self.max_val):
                raise ValueError(f"Field '{self.public_name}' must be integer between {self.min_val} and {self.max_val}.")
            setattr(instance, self.private_name, value)

    class UserAccount:
        username = StringField()
        age = IntegerField(min_val=18, max_val=120)

        def __init__(self, username: str, age: int):
            self.username = username
            self.age = age

    user = UserAccount("  alex_dev  ", 25)
    print(f"Validated user: '{user.username}', Age: {user.age}")

    try:
        user.age = 15  # Raises ValueError
    except ValueError as err:
        print("[DESCRIPTOR VALIDATION FAILED]", err)

def example_2():
    """
    Example 2: Auto-Registering Plugin Architecture via `__init_subclass__`
    """
    print("-" * 50)
    print("Running Example 2: Auto-Registering Plugin Architecture via `__init_subclass__`")
    print("-" * 50)
    class PaymentProcessorPlugin:
        registry = {}

        def __init_subclass__(cls, provider_id: str = None, **kwargs):
            super().__init_subclass__(**kwargs)
            if not provider_id:
                raise TypeError(f"Plugin '{cls.__name__}' must specify a 'provider_id'")
            if provider_id in cls.registry:
                raise ValueError(f"Duplicate provider_id '{provider_id}' already registered!")
            cls.registry[provider_id] = cls
            print(f"[PLUGIN SYSTEM] Registered payment provider: '{provider_id}'")

        def process(self, amount: float) -> str:
            raise NotImplementedError

    class StripePlugin(PaymentProcessorPlugin, provider_id="stripe"):
        def process(self, amount: float):
            return f"Charged ${amount:.2f} via Stripe API"

    class PayPalPlugin(PaymentProcessorPlugin, provider_id="paypal"):
        def process(self, amount: float):
            return f"Charged ${amount:.2f} via PayPal API"

    print("Active Plugins:", list(PaymentProcessorPlugin.registry.keys()))
    processor = PaymentProcessorPlugin.registry["stripe"]()
    print(processor.process(99.95))

def example_3():
    """
    Example 3: Dynamic API Proxy Client with `__getattr__`
    """
    print("-" * 50)
    print("Running Example 3: Dynamic API Proxy Client with `__getattr__`")
    print("-" * 50)
    class DynamicApiClient:
        def __init__(self, base_endpoint: str):
            self.base_endpoint = base_endpoint.rstrip("/")

        def __getattr__(self, endpoint_name: str):
            # Returns a callable that simulates requesting the endpoint
            def endpoint_caller(*args, **kwargs):
                full_url = f"{self.base_endpoint}/{endpoint_name.replace('_', '/')}"
                return {
                    "url": full_url,
                    "params": kwargs,
                    "status": "200_OK",
                    "message": f"Successfully queried endpoint: {endpoint_name}"
                }
            return endpoint_caller

    client = DynamicApiClient("https://api.internal.service/v1")
    # Calling non-existent methods dynamically intercepts:
    res1 = client.users_list(page=1, limit=10)
    res2 = client.orders_summary(user_id=884)

    print("Call 1:", res1["url"], res1["params"])
    print("Call 2:", res2["url"], res2["params"])

if __name__ == "__main__":
    print("=" * 60)
    print("Executing 9. Metaprogramming, Descriptors & Dynamic Python Examples")
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
    print("Completed 9. Metaprogramming, Descriptors & Dynamic Python Examples")
    print("=" * 60)
