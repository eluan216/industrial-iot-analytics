import sqlite3

conn = sqlite3.connect('slb_assets.db')
c = conn.cursor()

print('TABLES:', c.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall())
print('\nASSETS:')
for r in c.execute('SELECT id, name, serial_number, last_calibration_date, status FROM assets'):
    print(r)

conn.close()
