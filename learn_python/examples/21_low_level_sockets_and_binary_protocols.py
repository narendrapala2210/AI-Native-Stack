"""
Python Concept Examples: 21. Low-Level Systems: Sockets, Networking & Binary Protocols
Documentation Reference: ../21.low_level_sockets_and_binary_protocols.md
"""

import sys
import os

def example_1():
    """
    Example 1: Multi-Client Threaded TCP Chat Server & Client
    """
    print("-" * 50)
    print("Running Example 1: Multi-Client Threaded TCP Chat Server & Client")
    print("-" * 50)
    import socket
    import threading
    import time

    def handle_client(conn, addr):
        with conn:
            print(f"[THREAD] Handled connection from {addr}")
            while data := conn.recv(1024):
                conn.sendall(b"ECHO: " + data)

    def run_test_server(port=54321):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind(("127.0.0.1", port))
            s.listen(5)
            conn, addr = s.accept()
            handle_client(conn, addr)

    # Run server in background
    server_thread = threading.Thread(target=run_test_server, daemon=True)
    server_thread.start()
    time.sleep(0.02)

    # Client connects
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect(("127.0.0.1", 54321))
        client.sendall(b"Hello Server!")
        reply = client.recv(1024)
        print("Client received:", reply.decode())

def example_2():
    """
    Example 2: UDP Heartbeat Broadcast Monitor
    """
    print("-" * 50)
    print("Running Example 2: UDP Heartbeat Broadcast Monitor")
    print("-" * 50)
    import socket

    def send_heartbeat(node_id: str, port=54322):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            msg = f"HEARTBEAT:{node_id}".encode("utf-8")
            s.sendto(msg, ("127.0.0.1", port))

    def listen_heartbeat(port=54322):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.bind(("127.0.0.1", port))
            s.settimeout(0.5)
            try:
                data, addr = s.recvfrom(1024)
                print(f"[MONITOR] Node signal: {data.decode()} from {addr}")
            except socket.timeout:
                print("[MONITOR] No heartbeat signal detected within timeout.")

    # Test
    import threading
    threading.Thread(target=listen_heartbeat, daemon=True).start()
    time.sleep(0.01)
    send_heartbeat("worker-node-01")

def example_3():
    """
    Example 3: Binary Packet Marshaller with `struct`
    """
    print("-" * 50)
    print("Running Example 3: Binary Packet Marshaller with `struct`")
    print("-" * 50)
    import struct

    # Format: ! (Big-Endian network order), B (1-byte version), B (1-byte type), I (4-byte sequence), H (2-byte len)
    HEADER_FORMAT = "!BBIH"

    def pack_telemetry_header(version: int, packet_type: int, seq_id: int, payload_len: int) -> bytes:
        return struct.pack(HEADER_FORMAT, version, packet_type, seq_id, payload_len)

    def unpack_telemetry_header(raw_bytes: bytes) -> dict:
        version, p_type, seq, p_len = struct.unpack(HEADER_FORMAT, raw_bytes)
        return {"version": version, "type": p_type, "sequence": seq, "payload_len": p_len}

    packed = pack_telemetry_header(version=1, packet_type=5, seq_id=10248, payload_len=512)
    print("Binary Header (hex):", packed.hex())
    print("Unpacked Header:", unpack_telemetry_header(packed))

if __name__ == "__main__":
    print("=" * 60)
    print("Executing 21. Low-Level Systems: Sockets, Networking & Binary Protocols Examples")
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
    print("Completed 21. Low-Level Systems: Sockets, Networking & Binary Protocols Examples")
    print("=" * 60)
