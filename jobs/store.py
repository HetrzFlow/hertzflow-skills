"""Async job store (SQLite-backed)."""
import json, sqlite3, time

class JobStore:
    def __init__(self, path: str):
        self.conn = sqlite3.connect(path)
        self.conn.execute("CREATE TABLE IF NOT EXISTS jobs (id TEXT PRIMARY KEY, status TEXT, owner TEXT, report_url TEXT, created INTEGER)")

    def create(self, job_id: str, owner: str) -> None:
        self.conn.execute("INSERT INTO jobs VALUES (?,?,?,?,?)", (job_id, "queued", owner, None, int(time.time())))
        self.conn.commit()

    def update(self, job_id: str, status: str, report_url: str = None) -> None:
        self.conn.execute("UPDATE jobs SET status=?, report_url=COALESCE(?, report_url) WHERE id=?", (status, report_url, job_id))
        self.conn.commit()
