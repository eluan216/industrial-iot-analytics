import sqlite3
from datetime import datetime

DB_PATH = 'slb_assets.db'

def try_parse_date(s):
    s = str(s).strip()
    if not s:
        return None
    # Try ISO first
    try:
        dt = datetime.fromisoformat(s)
        return dt.date().isoformat()
    except Exception:
        pass
    # Common formats
    fmts = ['%Y-%m-%d', '%Y-%m-%d %H:%M:%S', '%d/%m/%Y', '%m/%d/%Y', '%d-%m-%Y', '%Y/%m/%d']
    for fm in fmts:
        try:
            dt = datetime.strptime(s, fm)
            return dt.date().isoformat()
        except Exception:
            continue
    # Try to handle RFC-like timestamp with T
    try:
        if 'T' in s:
            base = s.split('T')[0]
            dt = datetime.strptime(base, '%Y-%m-%d')
            return dt.date().isoformat()
    except Exception:
        pass
    return None


def normalize_db(path=DB_PATH):
    conn = sqlite3.connect(path)
    cur = conn.cursor()

    # Ensure table exists
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='assets';")
    if not cur.fetchone():
        print('No assets table found in database.')
        conn.close()
        return

    cur.execute('SELECT id, name, serial_number, last_calibration_date FROM assets')
    rows = cur.fetchall()
    print(f'Found {len(rows)} asset rows to inspect.')

    updated = 0
    for r in rows:
        _id, name, serial, last = r
        iso = try_parse_date(last)
        if iso is None and (last is None or str(last).strip() == ''):
            # leave blank
            continue
        if iso is None:
            print(f"Could not parse date for id={_id}, serial={serial}, value='{last}'")
            continue
        if iso != str(last):
            cur.execute('UPDATE assets SET last_calibration_date = ? WHERE id = ?', (iso, _id))
            updated += 1
            print(f"Updated id={_id} ({name}) from '{last}' -> '{iso}'")

    conn.commit()
    conn.close()
    print(f'Normalization complete. Rows updated: {updated}')

if __name__ == '__main__':
    normalize_db()
