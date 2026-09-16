# Industrial Analytics & Signal Intelligence Suite

**Author:** Oguma Eluanatein Odo  
**Focus:** Digital Signal Processing · Predictive Maintenance · Asset Integrity

---

## Quick Start (anyone can run this)

```bash
git clone https://github.com/eluan216/industrial-iot-analytics.git
cd industrial-iot-analytics
pip install -r requirements.txt

python sensor_signal_filter.py      # DSP demo — saves signal_processing_result.png
python predictive_maintenance.py    # ML demo — synthetic data, no download needed
python asset_integrity_manager.py   # SQL calibration audit
```

All three scripts run offline with no external dataset downloads.

---

## Overview

Applied data science and signal processing for industrial environments (oil & gas / sensor-heavy operations):

1. **Signal integrity** — cleaning noisy sensor telemetry with DSP
2. **Predictive maintenance** — classifying machine failure risk with Random Forest
3. **Asset integrity** — tracking calibration compliance with SQL

Skills transfer directly from biomedical signal processing to industrial systems.

---

## Project 1 — Digital Signal Processing (Sensor Integrity)

**File:** `sensor_signal_filter.py`

Simulates a clean 5 Hz process signal with high-frequency noise, then recovers it using a 5th-order Butterworth low-pass filter (zero-phase via `filtfilt`).

**Concepts:** Nyquist frequency, cutoff tuning, zero-phase filtering  
**Stack:** NumPy · SciPy · Matplotlib

---

## Project 2 — Predictive Maintenance (Machine Failure Classification)

**File:** `predictive_maintenance.py`

Trains a Random Forest classifier on synthetic industrial-style process data (temperature, torque, speed, tool wear). Optional: pass a real CSV path (e.g. AI4I 2020) with matching column names.

```bash
python predictive_maintenance.py
# or with real data:
python predictive_maintenance.py path/to/ai4i2020.csv
```

**Metrics:** Accuracy, weighted F1, classification report, feature importance  
**Stack:** Pandas · scikit-learn

---

## Project 3 — Asset Integrity & Calibration Tracking

**File:** `asset_integrity_manager.py`

Python + SQLite tool that tracks industrial assets and flags tools past a 180-day calibration window. Produces a Pass/Fail readiness report.

**Concepts:** Relational data, CRUD, compliance automation

---

## Repository Structure

```text
industrial-iot-analytics/
├── sensor_signal_filter.py      # DSP noise reduction demo
├── predictive_maintenance.py    # Random Forest failure prediction
├── asset_integrity_manager.py   # SQL calibration tracker
├── requirements.txt
├── assets/
└── signal_processing_result.png
```

---

## Why This Matters

- Clean sensor data is a prerequisite for reliable downstream ML
- Predictive maintenance reduces unplanned downtime (NPT)
- Calibration tracking protects data quality and operational compliance

Same principles as biomedical instrumentation: high SNR, rigorous evaluation, operational readiness.

---

## Author

**Oguma Eluanatein Odo**  
B.Sc. Biomedical Technology  
[LinkedIn](https://linkedin.com/in/eluanatein-oguma-5552571b6) · [GitHub](https://github.com/eluan216) · ogumaeluan@gmail.com

---

## License

MIT
