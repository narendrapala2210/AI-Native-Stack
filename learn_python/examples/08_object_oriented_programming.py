"""
Python Concept Examples: 8. Object-Oriented Programming (OOP) Deep Dive
Documentation Reference: ../08.object_oriented_programming.md
"""

import sys
import os

def example_1():
    """
    Example 1: Multi-Currency Money Class with Full Operator Overloading
    """
    print("-" * 50)
    print("Running Example 1: Multi-Currency Money Class with Full Operator Overloading")
    print("-" * 50)
    from decimal import Decimal

    class Money:
        __slots__ = ("_amount", "_currency")

        def __init__(self, amount: str | float | Decimal, currency: str = "USD"):
            self._amount = Decimal(str(amount)).quantize(Decimal("0.01"))
            self._currency = currency.upper()

        @property
        def amount(self) -> Decimal:
            return self._amount

        @property
        def currency(self) -> str:
            return self._currency

        def __repr__(self):
            return f"Money('{self._amount}', '{self._currency}')"

        def __str__(self):
            return f"{self._amount} {self._currency}"

        def __add__(self, other):
            if not isinstance(other, Money) or self._currency != other._currency:
                raise ValueError(f"Cannot add {self._currency} and {getattr(other, 'currency', type(other))}")
            return Money(self._amount + other._amount, self._currency)

        def __mul__(self, factor: float | int):
            return Money(self._amount * Decimal(str(factor)), self._currency)

        def __eq__(self, other):
            return isinstance(other, Money) and self._amount == other._amount and self._currency == other._currency

        def __lt__(self, other):
            if not isinstance(other, Money) or self._currency != other._currency:
                raise ValueError("Cannot compare distinct currencies")
            return self._amount < other._amount

    price1 = Money("49.95", "USD")
    price2 = Money("15.00", "USD")
    total = (price1 + price2) * 2

    print("Total price:", total)
    print("price1 > price2:", price1 > price2)

def example_2():
    """
    Example 2: Enterprise Entity Repository using Abstract Base Classes
    """
    print("-" * 50)
    print("Running Example 2: Enterprise Entity Repository using Abstract Base Classes")
    print("-" * 50)
    from abc import ABC, abstractmethod
    from typing import Optional, List

    class UserRepository(ABC):
        @abstractmethod
        def get_by_id(self, user_id: int) -> Optional[dict]:
            # Fetch user record by ID.
            pass

        @abstractmethod
        def save(self, user: dict) -> None:
            # Persist or update user record.
            pass

    class InMemoryUserRepository(UserRepository):
        def __init__(self):
            self._db = {}

        def get_by_id(self, user_id: int) -> Optional[dict]:
            return self._db.get(user_id)

        def save(self, user: dict) -> None:
            self._db[user["id"]] = user
            print(f"Saved user: {user['username']}")

    repo = InMemoryUserRepository()
    repo.save({"id": 101, "username": "claire"})
    print("Fetched:", repo.get_by_id(101))

def example_3():
    """
    Example 3: Memory-Optimized Point Cloud with `__slots__` and `@dataclass`
    """
    print("-" * 50)
    print("Running Example 3: Memory-Optimized Point Cloud with `__slots__` and `@dataclass`")
    print("-" * 50)
    from dataclasses import dataclass
    import sys

    @dataclass(slots=True, frozen=True)
    class SpatialPoint:
        x: float
        y: float
        z: float

        def distance_from_origin(self) -> float:
            return (self.x**2 + self.y**2 + self.z**2) ** 0.5

    p = SpatialPoint(1.5, 2.0, 3.5)
    print(f"Point: {p}, Distance: {p.distance_from_origin():.2f}")
    print("Point object memory footprint:", sys.getsizeof(p), "bytes")

if __name__ == "__main__":
    print("=" * 60)
    print("Executing 8. Object-Oriented Programming (OOP) Deep Dive Examples")
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
    print("Completed 8. Object-Oriented Programming (OOP) Deep Dive Examples")
    print("=" * 60)
