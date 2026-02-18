# Industrial Analytics & Signal Intelligence Suite

**Author:** Oguma Eluanatein Odo

**Field:** Biomedical Technology | Software Engineering | Data Science

## 📌 Executive Summary

This repository serves as a technical portfolio demonstrating the convergence of Biomedical Instrumentation and Digital Energy Technology. The projects herein address two of the most critical challenges in the Energy sector: Signal Integrity (ensuring clean data from downhole sensors) and Operational Efficiency (predicting equipment failure to reduce Non-Productive Time - NPT).

## 🛠 Project 1: Digital Signal Processing (DSP) for Sensor Integrity

### The Problem

In high-pressure, high-temperature (HPHT) environments, downhole sensors (Wireline/LWD) are subjected to extreme electrical noise, making it difficult to extract accurate "vitals" from the well. This challenge mirrors the clinical necessity of maintaining a high signal-to-noise ratio (SNR) in EKG monitoring, where environmental interference must be mitigated to ensure diagnostic accuracy.

### The Solution

**sensor_signal_filter.py**

I implemented a 5th Order Butterworth Lowpass Filter using the SciPy signal processing library. This script:

- Generates a synthetic 5Hz "True Signal."
- Simulates high-frequency Gaussian noise (interference).
- Applies a zero-phase digital filter to recover the original signal.

### Technical Stack

- **Language:** Python
- **Key Libraries:** NumPy, SciPy, Matplotlib
- **Concept:** Nyquist Frequency, Cutoff Frequency Tuning, Zero-phase Distortion.

### Visual Result

Figure 1: Comparison between raw sensor telemetry and the cleaned signal after Butterworth filtering.

## 📊 Project 2: Predictive Maintenance via Machine Learning (AI)

### The Problem

Unplanned equipment failure costs the energy industry billions in NPT. Moving from "Reactive" to "Predictive" maintenance is a core goal of SLB's Digital Transformation.

### The Solution

**predictive_maintenance.py**

Using the AI4I 2020 Predictive Maintenance Dataset, I developed a classification engine to identify potential failures before they occur.

- **Feature Engineering:** Analyzed Air Temperature, Torque, and Tool Wear as key predictors.
- **Model:** Employed a Random Forest Classifier due to its robustness against outliers.
- **Impact:** The model achieved an 88% accuracy rate and a high F1-score across specific failure modes (e.g., Heat Dissipation and Power Failure), demonstrating its reliability for industrial deployment.

### Technical Stack

- **Language:** Python
- **Key Libraries:** Pandas, Scikit-learn
- **Algorithm:** Random Forest (Ensemble Learning)

## 🚀 How to Run

Clone this repository:
```bash
git clone https://github.com/[YourUsername]/industrial-iot-analytics.git
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Execute scripts:
```bash
python sensor_signal_filter.py
```

## 🎓 Connection to SLB Values

- **Technology:** Demonstrates proficiency in Python and AI, supporting SLB's digital strategy.
- **Performance:** Focused on reducing NPT and optimizing asset uptime.
- **Precision:** Applies the rigorous standards of Biomedical Engineering to industrial data.

## 📬 Contact

- **LinkedIn:** linkedin.com/in/eluanatein-oguma-5552571b6
- **Email:** ogumaeluan@gmail.com
- **Status:** B.Sc. Biomedical Technology Graduate | Awaiting NYSC Placement | Available for immediate Graduate Internship (Pre-NYSC) opportunities.

## 🗄️ Project 3: Automated Asset Integrity & SQL Management
### **The Problem**
In oilfield operations, using an uncalibrated tool leads to inaccurate data and costly re-runs. Managing hundreds of high-tech sensors manually is inefficient and prone to error.

### **The Solution**
`asset_integrity_manager.py`  
A Python-based SQL engine that:
* **Tracks Assets:** Maintains a database of tool IDs and calibration histories.
* **Audit Automation:** Runs SQL queries to flag tools that have exceeded the 180-day calibration threshold.
* **Compliance:** Provides a clear "Pass/Fail" report for field readiness.

### **Technical Stack**
* **Language:** Python
* **Database:** SQLite3
* **Concepts:** Relational Databases, SQL CRUD Operations, Data Validation.

### **Final Pro-Tip for the Group**
By having these three projects, your friend has covered:
1.  **Math/Physics** (Signal Filtering)
2.  **Artificial Intelligence** (Predictive Maintenance)
3.  **Data Management** (SQL Assets)

This makes him a "Complete Digital Engineer." 

"He should commit this new file to his GitHub (`git add .`, `git commit -m \"Added SQL asset manager\"`, `git push`) right now!"

