"""
Python Concept Examples: 1. Python Architecture, Execution & Memory Model
Documentation Reference: ../01.python_architecture_and_memory.md
"""

import sys
import os

def example_1():
    """
    Example 1: Circular Reference Memory Leak Detector & Reclamation
    """
    print("-" * 50)
    print("Running Example 1: Circular Reference Memory Leak Detector & Reclamation")
    print("-" * 50)
    import gc
    import sys

    class CacheNode:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.linked_node = None

    def build_circular_graph():
        node1 = CacheNode("primary", {"data": [1, 2, 3]})
        node2 = CacheNode("secondary", {"data": [4, 5, 6]})
        # Create cycle
        node1.linked_node = node2
        node2.linked_node = node1
        return id(node1), id(node2)

    # Verify leak without GC
    gc.disable()  # Temporarily pause automatic GC sweeps
    n1_id, n2_id = build_circular_graph()

    # Nodes are out of scope, but refcount is still 1 due to the cycle!
    print(f"Cycle created with IDs: {n1_id}, {n2_id}")

    # Manually trigger cyclic collector
    reclaimed = gc.collect()
    print(f"[CLEANUP] Cyclic GC reclaimed {reclaimed} unreachable cyclic objects.")
    gc.enable()

def example_2():
    """
    Example 2: Bytecode Disassembly & Opcode Frequency Analyzer
    """
    print("-" * 50)
    print("Running Example 2: Bytecode Disassembly & Opcode Frequency Analyzer")
    print("-" * 50)
    import dis
    from collections import Counter

    def complex_pipeline(items):
        return [x.upper() for x in items if len(x) > 3]

    # Disassemble and extract opcodes
    instructions = dis.get_instructions(complex_pipeline)
    op_counts = Counter(instr.opname for instr in instructions)

    print("Bytecode Opcode Frequency:")
    for opcode, count in op_counts.most_common(5):
        print(f"  {opcode:<20}: {count} occurrences")

def example_3():
    """
    Example 3: Identity-Based Caching Layer (Exploiting Interning)
    """
    print("-" * 50)
    print("Running Example 3: Identity-Based Caching Layer (Exploiting Interning)")
    print("-" * 50)
    import sys

    class IdentityCache:
        def __init__(self):
            self._store = {}

        def get_or_compute(self, key: str, compute_fn):
            # Intern string to ensure identical memory address
            interned_key = sys.intern(key)
            for cached_key, val in self._store.items():
                if cached_key is interned_key:  # Pointer comparison O(1)
                    return val, "CACHE_HIT"
            result = compute_fn(interned_key)
            self._store[interned_key] = result
            return result, "CACHE_MISS"

    cache = IdentityCache()
    expensive_calc = lambda k: f"Processed: {k}"

    val1, status1 = cache.get_or_compute("user_auth_token", expensive_calc)
    val2, status2 = cache.get_or_compute("user_auth_token", expensive_calc)

    print(f"Call 1: {status1} -> {val1}")
    print(f"Call 2: {status2} -> {val2}")

if __name__ == "__main__":
    print("=" * 60)
    print("Executing 1. Python Architecture, Execution & Memory Model Examples")
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
    print("Completed 1. Python Architecture, Execution & Memory Model Examples")
    print("=" * 60)
