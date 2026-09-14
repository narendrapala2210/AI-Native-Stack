"""
Python Concept Examples: 12. Modular Architecture, Packages & Virtual Environments
Documentation Reference: ../12.modules_packages_environments.md
"""

import sys
import os

def example_1():
    """
    Example 1: Dynamic Module Loader by File Path
    """
    print("-" * 50)
    print("Running Example 1: Dynamic Module Loader by File Path")
    print("-" * 50)
    import importlib.util
    import tempfile
    from pathlib import Path

    def load_module_from_path(module_name: str, file_path: Path):
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        if spec is None or spec.loader is None:
            raise ImportError(f"Cannot load module from {file_path}")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    with tempfile.TemporaryDirectory() as tmpdir:
        script_file = Path(tmpdir) / "dynamic_plugin.py"
        script_file.write_text("def run_task(): return 'Plugin executed successfully!'", encoding="utf-8")

        loaded_mod = load_module_from_path("custom_plugin", script_file)
        print("Dynamically invoked result:", loaded_mod.run_task())

def example_2():
    """
    Example 2: Package Dependency Verification Script
    """
    print("-" * 50)
    print("Running Example 2: Package Dependency Verification Script")
    print("-" * 50)
    import importlib.metadata

    def verify_installed_package(package_name: str):
        try:
            version = importlib.metadata.version(package_name)
            return {"package": package_name, "installed": True, "version": version}
        except importlib.metadata.PackageNotFoundError:
            return {"package": package_name, "installed": False, "version": None}

    for pkg in ["pip", "pydantic", "non_existent_fake_package"]:
        status = verify_installed_package(pkg)
        print(f"Package '{pkg:<25}': Installed={status['installed']}, Version={status['version']}")

def example_3():
    """
    Example 3: Virtual Environment Isolation Auditor
    """
    print("-" * 50)
    print("Running Example 3: Virtual Environment Isolation Auditor")
    print("-" * 50)
    import sys

    def audit_environment():
        is_venv = sys.prefix != sys.base_prefix
        return {
            "is_virtualenv": is_venv,
            "executable": sys.executable,
            "prefix": sys.prefix,
            "base_prefix": sys.base_prefix
        }

    audit = audit_environment()
    print(f"Running inside Virtual Environment? {audit['is_virtualenv']}")
    print(f"Active Interpreter: {audit['executable']}")

if __name__ == "__main__":
    print("=" * 60)
    print("Executing 12. Modular Architecture, Packages & Virtual Environments Examples")
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
    print("Completed 12. Modular Architecture, Packages & Virtual Environments Examples")
    print("=" * 60)
