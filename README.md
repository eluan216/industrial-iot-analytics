# Industrial Analytics & Signal Intelligence Suite

**Author:** Oguma Eluanatein Odo  
**Focus:** Digital Signal Processing · Predictive Maintenance · Asset Integrity

---

## Overview

This repository demonstrates applied data science and signal processing for industrial environments — especially oil & gas and sensor-heavy operations. It covers three practical problems:

1. **Signal integrity** — cleaning noisy sensor telemetry with DSP
2. **Predictive maintenance** — classifying machine failure risk with Random Forest
3. **Asset integrity** — tracking calibration compliance with SQL

These skills transfer directly from biomedical signal processing to industrial systems.

---

## Project 1 — Digital Signal Processing (Sensor Integrity)

**File:** `sensor_signal_filter.py`

Simulates a clean 5 Hz process signal contaminated with high-frequency noise, then recovers it using a 5th-order Butterworth low-pass filter (zero-phase via `filtfilt`).

**Concepts:** Nyquist frequency, cutoff tuning, zero-phase filtering  
**Stack:** NumPy · SciPy · Matplotlib

```bash
python sensor_signal_filter.py
```

Output is saved as `signal_processing_result.png`.

---

## Project 2 — Predictive Maintenance (Machine Failure Classification)

**File:** `predictive_maintenance.py`

Trains a Random Forest classifier on the AI4I 2020 Predictive Maintenance dataset to predict machine failure from temperature, torque, rotational speed, and tool wear.

**Stack:** Pandas · scikit-learn  
**Metrics:** Accuracy, weighted F1, per-class report, feature importance

```bash
# Place ai4i2020.csv in the working directory, then:
python predictive_maintenance.py
```

---

## Project 3 — Asset Integrity & Calibration Tracking

**File:** `asset_integrity_manager.py`

Python + SQLite tool that tracks industrial assets and flags tools that have exceeded a 180-day calibration window. Produces a clear Pass/Fail readiness report.

**Concepts:** Relational data, CRUD, compliance automation

---

## Quick Start

```bash
git clone https://github.com/eluan216/industrial-iot-analytics.git
cd industrial-iot-analytics
pip install -r requirements.txt

# Run DSP demo
python sensor_signal_filter.py

# Run predictive maintenance (requires dataset)
python predictive_maintenance.py

# Run asset integrity manager
python asset_integrity_manager.py
```

---

## Repository Structure

```text
industrial-iot-analytics/
├── sensor_signal_filter.py      # DSP noise reduction demo
├── predictive_maintenance.py    # Random Forest failure prediction
├── asset_integrity_manager.py   # SQL calibration tracker
├── requirements.txt
├── assets/                      # Supporting images
└── signal_processing_result.png # Example DSP output
```

---

## Why This Matters

- Clean sensor data is a prerequisite for reliable downstream ML
- Predictive maintenance reduces unplanned downtime (NPT)
- Calibration tracking protects data quality and operational compliance

These are the same principles used in biomedical instrumentation — high SNR, rigorous evaluation, and operational readiness.

---

## Author

**Oguma Eluanatein Odo**  
B.Sc. Biomedical Technology  
[LinkedIn](https://linkedin.com/in/eluanatein-oguma-5552571b6) · [GitHub](https://github.com/eluan216) · ogumaeluan@gmail.com

---

## License

MIT
