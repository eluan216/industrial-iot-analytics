# scripts

This directory contains utility scripts for managing the local `slb_assets.db` SQLite database.

Available scripts:

- `inspect_slb_db.py` — prints tables and rows in `slb_assets.db` for quick inspection.
- `normalize_slb_assets_db.py` — attempts to parse and normalize `last_calibration_date` values into ISO `YYYY-MM-DD` format.

Usage (from project root):

```bash
# Inspect DB
.venv\Scripts\python.exe scripts\inspect_slb_db.py

# Normalize dates
.venv\Scripts\python.exe scripts\normalize_slb_assets_db.py
```

Notes:
- Back up `slb_assets.db` before running normalization in production.
- These scripts are small utilities and intended for local maintenance.
