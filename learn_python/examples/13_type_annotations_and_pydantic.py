"""
Python Concept Examples: 13. Modern Type Annotations & Pydantic Validation
Documentation Reference: ../13.type_annotations_and_pydantic.md
"""

import sys
import os

def example_1():
    """
    Example 1: Microservice Request/Response Schema with Pydantic v2
    """
    print("-" * 50)
    print("Running Example 1: Microservice Request/Response Schema with Pydantic v2")
    print("-" * 50)
    from pydantic import BaseModel, Field, field_validator
    from typing import List

    class OrderItem(BaseModel):
        sku: str = Field(min_length=3, max_length=12)
        quantity: int = Field(gt=0, le=100)
        price: float = Field(gt=0.0)

    class OrderCheckoutPayload(BaseModel):
        customer_id: int
        items: List[OrderItem] = Field(min_length=1)

        @field_validator("items")
        @classmethod
        def validate_unique_skus(cls, items: List[OrderItem]):
            skus = [i.sku for i in items]
            if len(skus) != len(set(skus)):
                raise ValueError("Duplicate SKUs detected in order items!")
            return items

        @property
        def total_cost(self) -> float:
            return sum(item.quantity * item.price for item in self.items)

    payload = {
        "customer_id": 1002,
        "items": [
            {"sku": "SKU-A01", "quantity": 2, "price": 29.99},
            {"sku": "SKU-B02", "quantity": 1, "price": 49.99}
        ]
    }

    order = OrderCheckoutPayload.model_validate(payload)
    print(f"Order valid! Customer: {order.customer_id}, Total: ${order.total_cost:.2f}")

def example_2():
    """
    Example 2: Structural Subtyping Plugin System with `typing.Protocol`
    """
    print("-" * 50)
    print("Running Example 2: Structural Subtyping Plugin System with `typing.Protocol`")
    print("-" * 50)
    from typing import Protocol

    class MessageNotifier(Protocol):
        def send_notification(self, recipient: str, body: str) -> bool:
            ...

    # Unrelated classes that satisfy the Protocol implicitly:
    class SlackService:
        def send_notification(self, recipient: str, body: str) -> bool:
            print(f"[SLACK to #{recipient}]: {body}")
            return True

    class DiscordService:
        def send_notification(self, recipient: str, body: str) -> bool:
            print(f"[DISCORD to @{recipient}]: {body}")
            return True

    def notify_user(notifier: MessageNotifier, user: str, msg: str):
        notifier.send_notification(user, msg)

    notify_user(SlackService(), "alerts", "Build 402 succeeded")
    notify_user(DiscordService(), "dev-chat", "Deployment complete")

def example_3():
    """
    Example 3: Generic In-Memory Thread-Safe Cache with `Generic[T]`
    """
    print("-" * 50)
    print("Running Example 3: Generic In-Memory Thread-Safe Cache with `Generic[T]`")
    print("-" * 50)
    from threading import Lock

    class GenericCache[T]:
        def __init__(self):
            self._store: dict[str, T] = {}
            self._lock = Lock()

        def set(self, key: str, value: T) -> None:
            with self._lock:
                self._store[key] = value

        def get(self, key: str) -> T | None:
            with self._lock:
                return self._store.get(key)

    # Type-safe integer cache
    int_cache = GenericCache[int]()
    int_cache.set("count", 42)
    print("Int cache value:", int_cache.get("count"))

    # Type-safe string cache
    str_cache = GenericCache[str]()
    str_cache.set("status", "HEALTHY")
    print("Str cache value:", str_cache.get("status"))

if __name__ == "__main__":
    print("=" * 60)
    print("Executing 13. Modern Type Annotations & Pydantic Validation Examples")
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
    print("Completed 13. Modern Type Annotations & Pydantic Validation Examples")
    print("=" * 60)
