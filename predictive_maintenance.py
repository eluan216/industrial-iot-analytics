"""
Predictive Maintenance — Industrial / Oil & Gas style demo

Trains a Random Forest classifier to predict machine failure from process features.
Uses synthetic industrial-style data by default so anyone can run it with no downloads.

Usage:
    pip install -r requirements.txt
    python predictive_maintenance.py

Optional: pass a real CSV path (e.g. AI4I 2020) with matching column names.
"""

from __future__ import annotations

import sys

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, f1_score
from sklearn.model_selection import train_test_split

FEATURES = [
    "Air temperature [K]",
    "Process temperature [K]",
    "Rotational speed [rpm]",
    "Torque [Nm]",
    "Tool wear [min]",
]
TARGET = "Machine failure"


def generate_synthetic_industrial_data(n_samples: int = 2000, seed: int = 42) -> pd.DataFrame:
    """Generate synthetic process data similar to industrial predictive-maintenance datasets."""
    rng = np.random.default_rng(seed)

    air_temp = rng.normal(300, 2, n_samples)
    process_temp = air_temp + rng.normal(10, 1, n_samples)
    rotational_speed = rng.normal(1500, 100, n_samples)
    torque = rng.normal(40, 10, n_samples)
    tool_wear = rng.uniform(0, 250, n_samples)

    risk = (
        0.015 * (torque - 40)
        + 0.008 * (tool_wear - 100)
        + 0.02 * np.abs(air_temp - 300)
        + 0.001 * np.abs(rotational_speed - 1500)
        + rng.normal(0, 0.5, n_samples)
    )
    failure = (risk > 1.2).astype(int)

    return pd.DataFrame(
        {
            "Air temperature [K]": air_temp.round(2),
            "Process temperature [K]": process_temp.round(2),
            "Rotational speed [rpm]": rotational_speed.round(1),
            "Torque [Nm]": torque.round(2),
            "Tool wear [min]": tool_wear.round(1),
            "Machine failure": failure,
        }
    )


def load_data(path: str | None = None) -> pd.DataFrame:
    if path:
        df = pd.read_csv(path)
        missing = [c for c in FEATURES + [TARGET] if c not in df.columns]
        if missing:
            raise ValueError(f"Missing columns in {path}: {missing}")
        return df
    return generate_synthetic_industrial_data()


def train_and_evaluate(df: pd.DataFrame) -> RandomForestClassifier:
    X = df[FEATURES]
    y = df[TARGET]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    model = RandomForestClassifier(
        n_estimators=100,
        max_depth=12,
        random_state=42,
        class_weight="balanced",
    )
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    f1 = f1_score(y_test, preds, average="weighted")

    print("=" * 50)
    print("PREDICTIVE MAINTENANCE — INDUSTRIAL DEMO")
    print("=" * 50)
    print(f"Samples: {len(df)} | Features: {len(FEATURES)}")
    print(f"Failure rate: {y.mean():.1%}")
    print(f"Accuracy:     {acc:.2%}")
    print(f"Weighted F1:  {f1:.4f}")
    print("\nClassification Report:")
    print(classification_report(y_test, preds, target_names=["No Failure", "Failure"]))
    print("Feature Importance:")
    for name, imp in sorted(zip(FEATURES, model.feature_importances_), key=lambda x: -x[1]):
        print(f"  {name}: {imp:.4f}")
    print("=" * 50)
    return model


if __name__ == "__main__":
    csv_path = sys.argv[1] if len(sys.argv) > 1 else None
    data = load_data(csv_path)
    train_and_evaluate(data)
    if csv_path is None:
        print("\nRan on synthetic data (no download required).")
        print("Optional: python predictive_maintenance.py path/to/ai4i2020.csv")
