"""
Python Concept Examples: 17. Pythonic Design Patterns: Creational, Structural & Behavioral
Documentation Reference: ../17.pythonic_design_patterns.md
"""

import sys
import os

def example_1():
    """
    Example 1: Thread-Safe Database Connection Pool (Singleton Pattern)
    """
    print("-" * 50)
    print("Running Example 1: Thread-Safe Database Connection Pool (Singleton Pattern)")
    print("-" * 50)
    import threading

    class ThreadSafeSingletonMeta(type):
        _instances = {}
        _lock = threading.Lock()

        def __call__(cls, *args, **kwargs):
            with cls._lock:
                if cls not in cls._instances:
                    cls._instances[cls] = super().__call__(*args, **kwargs)
            return cls._instances[cls]

    class DatabasePool(metaclass=ThreadSafeSingletonMeta):
        def __init__(self):
            self.pool_id = "POOL-MAIN-001"
            self.max_connections = 10

    pool_a = DatabasePool()
    pool_b = DatabasePool()
    print("Are both connection pools identical?", pool_a is pool_b)  # True
    print(f"Pool ID: {pool_a.pool_id}")

def example_2():
    """
    Example 2: Dynamic Payment Gateway Selector (Strategy Pattern)
    """
    print("-" * 50)
    print("Running Example 2: Dynamic Payment Gateway Selector (Strategy Pattern)")
    print("-" * 50)
    from typing import Callable

    # Strategies as clean functions
    def process_stripe(amount: float) -> str:
        return f"Paid ${amount:.2f} via Stripe card processing"

    def process_crypto(amount: float) -> str:
        return f"Paid ${amount:.2f} via Ethereum smart contract"

    class PaymentCheckout:
        def __init__(self, processor_strategy: Callable[[float], str]):
            self.strategy = processor_strategy

        def checkout(self, amount: float) -> str:
            return self.strategy(amount)

    checkout_card = PaymentCheckout(process_stripe)
    print(checkout_card.checkout(150.0))

    checkout_web3 = PaymentCheckout(process_crypto)
    print(checkout_web3.checkout(150.0))

def example_3():
    """
    Example 3: Real-Time Event Dispatcher (Observer / Pub-Sub Pattern)
    """
    print("-" * 50)
    print("Running Example 3: Real-Time Event Dispatcher (Observer / Pub-Sub Pattern)")
    print("-" * 50)
    class EventDispatcher:
        def __init__(self):
            self._listeners = {}

        def subscribe(self, event_name: str, callback):
            self._listeners.setdefault(event_name, []).append(callback)

        def dispatch(self, event_name: str, payload: dict):
            for callback in self._listeners.get(event_name, []):
                callback(payload)

    # Observers
    def notify_slack(data):
        print(f"[SLACK ALERT] Deployment of {data['service']} completed!")

    def update_metrics(data):
        print(f"[DATADOG METRIC] increment_counter('deploys', tags=['{data['service']}'])")

    dispatcher = EventDispatcher()
    dispatcher.subscribe("deploy_success", notify_slack)
    dispatcher.subscribe("deploy_success", update_metrics)

    dispatcher.dispatch("deploy_success", {"service": "AuthService_v2"})

if __name__ == "__main__":
    print("=" * 60)
    print("Executing 17. Pythonic Design Patterns: Creational, Structural & Behavioral Examples")
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
    print("Completed 17. Pythonic Design Patterns: Creational, Structural & Behavioral Examples")
    print("=" * 60)
