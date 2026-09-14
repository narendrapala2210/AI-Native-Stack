"""
Python Concept Examples: 11. File I/O, Serialization & SQLite
Documentation Reference: ../11.file_io_serialization_sqlite.md
"""

import sys
import os

def example_1():
    """
    Example 1: Atomic JSON Configuration Store with Backup & Restore
    """
    print("-" * 50)
    print("Running Example 1: Atomic JSON Configuration Store with Backup & Restore")
    print("-" * 50)
    import json
    import shutil
    from pathlib import Path

    class ConfigStore:
        def __init__(self, file_path: str):
            self.file_path = Path(file_path)
            self.backup_path = self.file_path.with_suffix(".bak")

        def save(self, data: dict):
            if self.file_path.exists():
                shutil.copy2(self.file_path, self.backup_path)  # Backup existing
            self.file_path.write_text(json.dumps(data, indent=2), encoding="utf-8")
            print(f"Saved configuration to {self.file_path}")

        def load(self) -> dict:
            try:
                return json.loads(self.file_path.read_text(encoding="utf-8"))
            except (FileNotFoundError, json.JSONDecodeError):
                if self.backup_path.exists():
                    print("[RECOVERY] Primary config corrupted; restoring from backup...")
                    return json.loads(self.backup_path.read_text(encoding="utf-8"))
                return {}

    cfg = ConfigStore("app_config.json")
    cfg.save({"env": "production", "workers": 4})
    print("Loaded config:", cfg.load())

    # Cleanup
    cfg.file_path.unlink(missing_ok=True)
    cfg.backup_path.unlink(missing_ok=True)

def example_2():
    """
    Example 2: Compressed Archive Backup System with `zipfile` and `pathlib`
    """
    print("-" * 50)
    print("Running Example 2: Compressed Archive Backup System with `zipfile` and `pathlib`")
    print("-" * 50)
    import zipfile
    from pathlib import Path
    import tempfile

    def create_project_archive(source_dir: Path, output_zip: Path, file_extension: str = "*.py"):
        with zipfile.ZipFile(output_zip, mode="w", compression=zipfile.ZIP_DEFLATED) as archive:
            for file in source_dir.rglob(file_extension):
                archive_name = file.relative_to(source_dir)
                archive.write(file, arcname=archive_name)
                print(f"Archived: {archive_name}")

    with tempfile.TemporaryDirectory() as tmpdir:
        src = Path(tmpdir) / "project"
        src.mkdir()
        (src / "main.py").write_text("print('hello')", encoding="utf-8")
        (src / "utils.py").write_text("def add(a,b): return a+b", encoding="utf-8")

        zip_out = Path(tmpdir) / "backup.zip"
        create_project_archive(src, zip_out)

        with zipfile.ZipFile(zip_out, "r") as zf:
            print("Archive verified contents:", zf.namelist())

def example_3():
    """
    Example 3: Embedded SQLite Key-Value Storage with Expiration TTL
    """
    print("-" * 50)
    print("Running Example 3: Embedded SQLite Key-Value Storage with Expiration TTL")
    print("-" * 50)
    import sqlite3
    import time

    class SQLiteCache:
        def __init__(self, db_path: str = ":memory:"):
            self.conn = sqlite3.connect(db_path)
            self.conn.execute("CREATE TABLE IF NOT EXISTS cache (key TEXT PRIMARY KEY, value TEXT, expires_at REAL)")
            self.conn.commit()

        def set(self, key: str, value: str, ttl_seconds: float = 60.0):
            expires_at = time.time() + ttl_seconds
            self.conn.execute("INSERT OR REPLACE INTO cache VALUES (?, ?, ?)", (key, value, expires_at))
            self.conn.commit()

        def get(self, key: str) -> str | None:
            cur = self.conn.cursor()
            cur.execute("SELECT value, expires_at FROM cache WHERE key = ?", (key,))
            row = cur.fetchone()
            if not row:
                return None
            val, expires_at = row
            if time.time() > expires_at:
                self.conn.execute("DELETE FROM cache WHERE key = ?", (key,))
                self.conn.commit()
                return None
            return val

    cache = SQLiteCache()
    cache.set("session_token", "secret_9988", ttl_seconds=0.05)
    print("Immediate fetch:", cache.get("session_token"))
    time.sleep(0.06)
    print("Fetch after TTL expiration:", cache.get("session_token"))  # None

if __name__ == "__main__":
    print("=" * 60)
    print("Executing 11. File I/O, Serialization & SQLite Examples")
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
    print("Completed 11. File I/O, Serialization & SQLite Examples")
    print("=" * 60)
