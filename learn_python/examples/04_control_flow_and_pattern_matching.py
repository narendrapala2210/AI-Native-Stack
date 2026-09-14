"""
Python Concept Examples: 4. Control Flow & Structural Pattern Matching
Documentation Reference: ../04.control_flow_and_pattern_matching.md
"""

import sys
import os

def example_1():
    """
    Example 1: Microservice Event Router with Structural Pattern Matching
    """
    print("-" * 50)
    print("Running Example 1: Microservice Event Router with Structural Pattern Matching")
    print("-" * 50)
    def route_event(event: dict) -> str:
        match event:
            # Match user creation with positive user_id
            case {"type": "USER_CREATED", "payload": {"id": int(uid), "email": str(email)}} if uid > 0:
                return f"Creating user profile for {email} (UID: {uid})"

            # Match order placed with total value
            case {"type": "ORDER_PLACED", "payload": {"order_id": str(oid), "total": float(amt)}}:
                return f"Processing order {oid} for ${amt:.2f}"

            # Match failure alerts with error codes
            case {"type": "SYSTEM_ALERT", "level": "CRITICAL" | "FATAL", "error_code": code}:
                return f"PAGING ON-CALL ENGINEER! Error Code: {code}"

            # Fallback wildcard
            case _:
                return "Discarding unrecognized event schema."

    print(route_event({"type": "USER_CREATED", "payload": {"id": 42, "email": "alex@dev.internal"}}))
    print(route_event({"type": "SYSTEM_ALERT", "level": "CRITICAL", "error_code": 503}))
    print(route_event({"type": "UNKNOWN"}))

def example_2():
    """
    Example 2: Network Client Exponential Backoff with Loop-`else`
    """
    print("-" * 50)
    print("Running Example 2: Network Client Exponential Backoff with Loop-`else`")
    print("-" * 50)
    import time
    import random

    def simulated_unstable_api_call():
        # Fails 80% of the time
        if random.random() < 0.8:
            raise ConnectionError("Network reset by peer")
        return {"status": "SUCCESS", "data": "Cluster Metrics"}

    def fetch_with_backoff(max_retries: int = 3) -> dict:
        delay = 0.05
        for attempt in range(1, max_retries + 1):
            try:
                print(f"[ATTEMPT {attempt}] Contacting remote API...")
                return simulated_unstable_api_call()
            except ConnectionError as err:
                print(f"Attempt {attempt} failed: {err}. Retrying in {delay:.2f}s...")
                time.sleep(delay)
                delay *= 2  # Exponential backoff
        else:
            # Only reached if loop terminates without hitting the return!
            raise TimeoutError(f"Remote API completely unreachable after {max_retries} attempts.")

    try:
        data = fetch_with_backoff(max_retries=3)
        print("Fetched successfully:", data)
    except TimeoutError as te:
        print("[FINAL ERROR]", te)

def example_3():
    """
    Example 3: Chunked Batch Processor with `zip` and `enumerate`
    """
    print("-" * 50)
    print("Running Example 3: Chunked Batch Processor with `zip` and `enumerate`")
    print("-" * 50)
    def chunked_iterable(iterable, chunk_size: int):
        iterator = iter(iterable)
        while batch := list(zip(*[iterator] * chunk_size)):
            yield batch[0] if chunk_size == 1 else batch

    data_stream = list(range(1, 13))
    batch_size = 4

    for batch_idx, batch in enumerate(zip(*[iter(data_stream)] * batch_size), start=1):
        print(f"Batch #{batch_idx}: Executing bulk DB insert of items {batch}")

if __name__ == "__main__":
    print("=" * 60)
    print("Executing 4. Control Flow & Structural Pattern Matching Examples")
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
    print("Completed 4. Control Flow & Structural Pattern Matching Examples")
    print("=" * 60)
