"""
Python Concept Examples: 23. C-Extensions & Foreign Function Interoperability
Documentation Reference: ../23.c_extensions_and_ffi.md
"""

import sys
import os

def example_1():
    """
    Example 1: High-Speed Native Math Calls via `ctypes`
    """
    print("-" * 50)
    print("Running Example 1: High-Speed Native Math Calls via `ctypes`")
    print("-" * 50)
    import ctypes
    import os
    import math

    if os.name == "nt":
        libc = ctypes.cdll.msvcrt
    else:
        libc = ctypes.CDLL("libc.so.6")

    # Bind C math sqrt function
    libc.sqrt.argtypes = [ctypes.c_double]
    libc.sqrt.restype = ctypes.c_double

    val = 144.0
    c_res = libc.sqrt(val)
    print(f"Native C sqrt({val}) = {c_res}")

def example_2():
    """
    Example 2: C Struct Marshalling and Raw Pointer Manipulation
    """
    print("-" * 50)
    print("Running Example 2: C Struct Marshalling and Raw Pointer Manipulation")
    print("-" * 50)
    import ctypes

    class SensorData(ctypes.Structure):
        _fields_ = [
            ("sensor_id", ctypes.c_uint32),
            ("temperature", ctypes.c_float),
            ("active", ctypes.c_bool)
        ]

    # Create instance
    reading = SensorData(sensor_id=8001, temperature=24.5, active=True)

    # Access pointer to struct
    ptr = ctypes.pointer(reading)

    print(f"Sensor ID: {ptr.contents.sensor_id}, Temp: {ptr.contents.temperature:.1f}°C")
    print(f"Pointer memory address: {ctypes.addressof(ptr.contents)}")

def example_3():
    """
    Example 3: C-Level Buffer Inspection and Size Validation
    """
    print("-" * 50)
    print("Running Example 3: C-Level Buffer Inspection and Size Validation")
    print("-" * 50)
    import ctypes

    class NetworkPacket(ctypes.BigEndianStructure):
        _fields_ = [
            ("magic", ctypes.c_uint16),
            ("code", ctypes.c_uint8),
            ("payload_size", ctypes.c_uint16)
        ]

    packet = NetworkPacket(magic=0xA1B2, code=4, payload_size=1024)
    buffer = bytes(packet)

    print(f"Network packet struct size: {ctypes.sizeof(packet)} bytes")
    print("Raw memory bytes (Hex):", buffer.hex())

if __name__ == "__main__":
    print("=" * 60)
    print("Executing 23. C-Extensions & Foreign Function Interoperability Examples")
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
    print("Completed 23. C-Extensions & Foreign Function Interoperability Examples")
    print("=" * 60)
