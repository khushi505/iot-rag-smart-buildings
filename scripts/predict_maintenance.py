# scripts/predict_maintenance.py

import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest

# Load your sensor data (replace with real-time ingestion later)
def load_sensor_data(csv_path: str):
    return pd.read_csv(csv_path)

def detect_anomalies(df: pd.DataFrame):
    features = ["temperature", "humidity", "vibration"]
    model = IsolationForest(contamination=0.05, random_state=42)
    df["anomaly"] = model.fit_predict(df[features])
    df["is_anomaly"] = df["anomaly"] == -1
    return df

if __name__ == "__main__":
    df = load_sensor_data("data/sensor_data.csv")
    df = detect_anomalies(df)

    anomalies = df[df["is_anomaly"]]
    if anomalies.empty:
        print("✅ No anomalies detected.")
    else:
        print(f"⚠️ {len(anomalies)} anomalies found:")
        print(anomalies[["timestamp", "temperature", "humidity", "vibration", "device_id"]])
