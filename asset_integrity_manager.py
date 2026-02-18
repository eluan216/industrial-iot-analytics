import sqlite3
from datetime import datetime, timedelta

def setup_asset_database():
    # Connect to (or create) the database file
    conn = sqlite3.connect('slb_assets.db')
    cursor = conn.cursor()

    # Create a table for laboratory/field assets
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS assets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            serial_number TEXT UNIQUE,
            last_calibration_date DATE,
            status TEXT
        )
    ''')

    # Add sample assets (Simulating SLB sensors and tools)
    # Use ISO-format strings for dates to ensure consistent storage and comparison
    sample_assets = [
        ('Gamma Ray Detector', 'SN-GR-001', (datetime.now() - timedelta(days=200)).date().isoformat(), 'Active'),
        ('Resistivity Tool', 'SN-RT-552', (datetime.now() - timedelta(days=30)).date().isoformat(), 'Active'),
        ('Pressure Transducer', 'SN-PT-990', (datetime.now() - timedelta(days=10)).date().isoformat(), 'Maintenance'),
        ('Density Sensor', 'SN-DS-441', (datetime.now() - timedelta(days=250)).date().isoformat(), 'Active')
    ]

    cursor.executemany('''
        INSERT OR IGNORE INTO assets (name, serial_number, last_calibration_date, status)
        VALUES (?, ?, ?, ?)
    ''', sample_assets)

    conn.commit()
    return conn

def run_calibration_audit(conn):
    cursor = conn.cursor()
    print("--- SLB ASSET INTEGRITY AUDIT ---")
    
    # Define the threshold (6 months / 180 days) and use ISO string for comparison
    threshold_date = (datetime.now() - timedelta(days=180)).date()
    threshold_iso = threshold_date.isoformat()

    # SQL Query to find expired assets (dates stored as ISO strings)
    cursor.execute("SELECT name, serial_number, last_calibration_date FROM assets WHERE last_calibration_date < ?", (threshold_iso,))

    expired_assets = cursor.fetchall()

    if expired_assets:
        print(f"\nWARNING: {len(expired_assets)} Assets require immediate re-calibration:\n")
        for asset in expired_assets:
            # last_calibration_date is stored as ISO string; convert to date for nicer output
            try:
                last_cal = datetime.fromisoformat(asset[2]).date()
            except Exception:
                last_cal = asset[2]
            print(f"FAILED: {asset[0]} ({asset[1]}) - Last Calibrated: {last_cal}")
    else:
        print("\nAll assets are within calibration limits.")
    
    conn.close()

if __name__ == "__main__":
    connection = setup_asset_database()
    run_calibration_audit(connection)