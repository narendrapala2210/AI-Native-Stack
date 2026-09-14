"""
Python Concept Examples: 15. Essential Standard Library Modules & CLI Tools
Documentation Reference: ../15.standard_library_and_cli_tools.md
"""

import sys
import os

def example_1():
    """
    Example 1: Production DevOps CLI with Subcommands via `argparse`
    """
    print("-" * 50)
    print("Running Example 1: Production DevOps CLI with Subcommands via `argparse`")
    print("-" * 50)
    import argparse

    def build_cli():
        parser = argparse.ArgumentParser(prog="cluster-tool", description="Cluster Deployment Utility")
        subparsers = parser.add_subparsers(dest="action", required=True)

        # Subcommand: deploy
        deploy_cmd = subparsers.add_parser("deploy", help="Deploy container to target cluster")
        deploy_cmd.add_argument("--cluster", required=True, choices=["us-east", "eu-central"])
        deploy_cmd.add_argument("--replicas", type=int, default=3)

        # Subcommand: teardown
        teardown_cmd = subparsers.add_parser("teardown", help="Teardown environment")
        teardown_cmd.add_argument("--force", action="store_true")

        return parser

    parser = build_cli()
    args = parser.parse_args(["deploy", "--cluster", "us-east", "--replicas", "5"])
    print(f"Action: {args.action}, Cluster: {args.cluster}, Replicas: {args.replicas}")

def example_2():
    """
    Example 2: Multi-Timezone International Meeting Coordinator
    """
    print("-" * 50)
    print("Running Example 2: Multi-Timezone International Meeting Coordinator")
    print("-" * 50)
    from datetime import datetime, timezone
    from zoneinfo import ZoneInfo

    def plan_global_meeting(year: int, month: int, day: int, hour: int, minute: int):
        # Scheduled time in London
        london_tz = ZoneInfo("Europe/London")
        meeting_london = datetime(year, month, day, hour, minute, tzinfo=london_tz)

        other_zones = [
            ("New York", ZoneInfo("America/New_York")),
            ("Tokyo", ZoneInfo("Asia/Tokyo")),
            ("San Francisco", ZoneInfo("America/Los_Angeles")),
            ("UTC Standard", timezone.utc)
        ]

        print(f"Meeting Origin (London): {meeting_london.strftime('%Y-%m-%d %H:%M %Z')}")
        print("Local Times for Participants:")
        for city, tz in other_zones:
            local_time = meeting_london.astimezone(tz)
            print(f"  {city:<15}: {local_time.strftime('%Y-%m-%d %H:%M %Z')}")

    plan_global_meeting(2026, 9, 15, 14, 0)

def example_3():
    """
    Example 3: Structured Access Log Parser with Named Regex Groups
    """
    print("-" * 50)
    print("Running Example 3: Structured Access Log Parser with Named Regex Groups")
    print("-" * 50)
    import re

    log_line = '192.168.1.50 - - [14/Sep/2026:12:00:00 +0000] "POST /api/v1/auth HTTP/1.1" 200 4096'

    pattern = re.compile(
        r'(?P<ip>\d+\.\d+\.\d+\.\d+)\s+-\s+-\s+'
        r'\[(?P<timestamp>[^\]]+)\]\s+'
        r'"(?P<method>[A-Z]+)\s+(?P<path>\S+)\s+(?P<protocol>[^"]+)"\s+'
        r'(?P<status>\d{3})\s+'
        r'(?P<bytes>\d+)'
    )

    match = pattern.match(log_line)
    if match:
        data = match.groupdict()
        print("Parsed Web Request:")
        for key, value in data.items():
            print(f"  {key:<12}: {value}")

if __name__ == "__main__":
    print("=" * 60)
    print("Executing 15. Essential Standard Library Modules & CLI Tools Examples")
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
    print("Completed 15. Essential Standard Library Modules & CLI Tools Examples")
    print("=" * 60)
