"""
Python Concept Examples: 7. Decorators & Functional Enhancements
Documentation Reference: ../07.decorators_and_functional_tools.md
"""

import sys
import os

def example_1():
    """
    Example 1: In-Memory TTL (Time-To-Live) Cache Decorator
    """
    print("-" * 50)
    print("Running Example 1: In-Memory TTL (Time-To-Live) Cache Decorator")
    print("-" * 50)
    import time
    from functools import wraps

    def ttl_cache(seconds: float):
        def decorator(func):
            cache = {}

            @wraps(func)
            def wrapper(*args, **kwargs):
                key = (args, tuple(sorted(kwargs.items())))
                now = time.time()
                if key in cache:
                    cached_val, timestamp = cache[key]
                    if now - timestamp < seconds:
                        print(f"[CACHE HIT] Returning cached value for {func.__name__}{args}")
                        return cached_val

                print(f"[CACHE MISS] Executing {func.__name__}{args}...")
                result = func(*args, **kwargs)
                cache[key] = (result, now)
                return result

            return wrapper
        return decorator

    @ttl_cache(seconds=0.1)
    def fetch_user_avatar(user_id: int):
        return f"https://cdn.internal/avatars/{user_id}.png"

    print(fetch_user_avatar(101))
    print(fetch_user_avatar(101))  # Cache hit!
    time.sleep(0.12)
    print(fetch_user_avatar(101))  # Expired, recalculates!

def example_2():
    """
    Example 2: Automatic Network Retry Decorator with Jitter
    """
    print("-" * 50)
    print("Running Example 2: Automatic Network Retry Decorator with Jitter")
    print("-" * 50)
    import time
    from functools import wraps

    def retry_on_exception(max_retries: int = 3, delay: float = 0.05, allowed_exceptions = (Exception,)):
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                for attempt in range(1, max_retries + 1):
                    try:
                        return func(*args, **kwargs)
                    except allowed_exceptions as e:
                        print(f"[RETRY] '{func.__name__}' failed (Attempt {attempt}/{max_retries}): {e}")
                        if attempt == max_retries:
                            raise
                        time.sleep(delay)
            return wrapper
        return decorator

    attempts_made = 0

    @retry_on_exception(max_retries=3, delay=0.02, allowed_exceptions=(ValueError,))
    def volatile_api_call():
        global attempts_made
        attempts_made += 1
        if attempts_made < 3:
            raise ValueError("Service temporarily unavailable")
        return "SUCCESS: Connected to API"

    print("Result:", volatile_api_call())

def example_3():
    """
    Example 3: Runtime Argument Type Enforcer
    """
    print("-" * 50)
    print("Running Example 3: Runtime Argument Type Enforcer")
    print("-" * 50)
    from functools import wraps
    import inspect

    def enforce_types(func):
        sig = inspect.signature(func)

        @wraps(func)
        def wrapper(*args, **kwargs):
            bound_args = sig.bind(*args, **kwargs)
            bound_args.apply_defaults()

            for name, value in bound_args.arguments.items():
                expected_type = sig.parameters[name].annotation
                if expected_type != inspect.Parameter.empty and not isinstance(value, expected_type):
                    raise TypeError(
                        f"Argument '{name}' must be of type {expected_type.__name__}, got {type(value).__name__}"
                    )
            return func(*args, **kwargs)

        return wrapper

    @enforce_types
    def register_student(name: str, age: int, gpa: float) -> str:
        return f"Student {name}, Age {age}, GPA {gpa}"

    print(register_student("Alice", 21, 3.9))
    try:
        register_student("Bob", "twenty-one", 3.5)  # Raises TypeError
    except TypeError as te:
        print("[TYPE VALIDATION FAILED]", te)

if __name__ == "__main__":
    print("=" * 60)
    print("Executing 7. Decorators & Functional Enhancements Examples")
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
    print("Completed 7. Decorators & Functional Enhancements Examples")
    print("=" * 60)
