import sqlite3
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

DB = 'slb_assets.db'
OUT = 'assets/project3_demo.gif'

def load_assets(db=DB):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute("SELECT id, name, last_calibration_date FROM assets ORDER BY id")
    rows = cur.fetchall()
    conn.close()
    assets = []
    for _id, name, last in rows:
        assets.append((name, last))
    return assets


def is_overdue(last_date_iso):
    try:
        last = datetime.fromisoformat(last_date_iso).date()
    except Exception:
        return False
    return (datetime.now().date() - last).days > 180


def make_animation(assets, out_path):
    names = [a[0] for a in assets]
    statuses = [is_overdue(a[1]) for a in assets]
    n = len(names)

    fig, ax = plt.subplots(figsize=(6, 2 + 0.6 * n))
    plt.tight_layout()

    y = np.arange(n)
    bar_containers = ax.barh(y, [1]*n, color=['green' if not s else 'red' for s in statuses])

    ax.set_xlim(0, 1)
    ax.set_yticks(y)
    ax.set_yticklabels(names)
    ax.set_xticks([])
    ax.invert_yaxis()
    ax.set_title('Asset Calibration Audit — Overdue assets pulse')

    def update(frame):
        # Pulse failed assets
        pulse = 0.6 + 0.4 * (np.sin(frame / 2.0) * 0.5 + 0.5)
        for i, b in enumerate(bar_containers):
            if statuses[i]:
                b.set_width(pulse)
                b.set_color((1.0, 0.2 + 0.6 * (frame % 2), 0.2))
            else:
                b.set_width(1.0)
                b.set_color((0.1, 0.6, 0.2))
        return bar_containers

    ani = animation.FuncAnimation(fig, update, frames=30, interval=150, blit=False)

    try:
        ani.save(out_path, writer='pillow', dpi=100)
    except Exception:
        # fallback to imageio if pillow writer unavailable
        ani.save(out_path, writer='imagemagick', dpi=100)

    plt.close(fig)


if __name__ == '__main__':
    assets = load_assets()
    if not assets:
        print('No assets found in DB; nothing to animate.')
    else:
        print(f'Creating animation for {len(assets)} assets...')
        make_animation(assets, OUT)
        print('Animation written to assets/project3_demo.gif')
