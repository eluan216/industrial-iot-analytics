import sqlite3
from datetime import datetime, timedelta

DB = 'slb_assets.db'

def recalibrate(db=DB):
    conn = sqlite3.connect(db)
    cur = conn.cursor()

    threshold = (datetime.now() - timedelta(days=180)).date().isoformat()
    cur.execute("SELECT id, name, serial_number, last_calibration_date, status FROM assets WHERE last_calibration_date < ?", (threshold,))
    rows = cur.fetchall()
    if not rows:
        print('No expired assets found.')
        conn.close()
        return

    today = datetime.now().date().isoformat()
    updated = 0
    for r in rows:
        _id, name, serial, last, status = r
        print(f"Updating id={_id}: {name} ({serial}) last_calibration_date {last} -> {today}, status {status} -> Active")
        cur.execute("UPDATE assets SET last_calibration_date = ?, status = ? WHERE id = ?", (today, 'Active', _id))
        updated += 1

    conn.commit()
    conn.close()
    print(f"Recalibration complete. Rows updated: {updated}")

if __name__ == '__main__':
    recalibrate()
