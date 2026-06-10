import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import joblib

# Load cleaned data and sort by time
df = pd.read_parquet("data/processed/02_cleaned.parquet").sort_values("timestamp")

# Features
feature_cols = ["temperature_c", "humidity_pct", "co2_ppm"]

# Chronological 80/20 split
split_idx = int(len(df) * 0.8)
train, test = df.iloc[:split_idx], df.iloc[split_idx:]

# Scale using TRAIN data only
scaler = MinMaxScaler()

X_train = scaler.fit_transform(train[feature_cols])
X_test = scaler.transform(test[feature_cols])

y_train = train["yield_kg"].values
y_test = test["yield_kg"].values

# Save scaler
joblib.dump(scaler, "models/scaler.joblib")

# Optional: Save train/test datasets
np.save("data/processed/X_train.npy", X_train)
np.save("data/processed/X_test.npy", X_test)
np.save("data/processed/y_train.npy", y_train)
np.save("data/processed/y_test.npy", y_test)

# Summary
print(f"Train: {train['timestamp'].min()} → {train['timestamp'].max()}")
print(f"Test:  {test['timestamp'].min()} → {test['timestamp'].max()}")
print("Train rows:", len(train))
print("Test rows:", len(test))

print("\nFiles saved:")
print("- models/scaler.joblib")
print("- data/processed/X_train.npy")
print("- data/processed/X_test.npy")
print("- data/processed/y_train.npy")
print("- data/processed/y_test.npy")