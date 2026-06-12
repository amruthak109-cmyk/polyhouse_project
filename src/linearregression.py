import pandas as pd
from sklearn.preprocessing import MinMaxScaler

df = pd.read_parquet("data/processed/02_cleaned.parquet").sort_values("timestamp")

feature_cols = ["temperature_c", "humidity_pct", "co2_ppm"]

split_idx = int(len(df) * 0.8)
train, test = df.iloc[:split_idx], df.iloc[split_idx:]

scaler = MinMaxScaler()

X_train = scaler.fit_transform(train[feature_cols])
X_test = scaler.transform(test[feature_cols])

y_train = train["yield_kg"].values
y_test = test["yield_kg"].values

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib
import numpy as np

model = LinearRegression()
model.fit(X_train, y_train)

pred_test = model.predict(X_test)

mae = mean_absolute_error(y_test, pred_test)
rmse = np.sqrt(mean_squared_error(y_test, pred_test))
r2 = r2_score(y_test, pred_test)

print(f"Test MAE: {mae:.2f} kg")
print(f"Test RMSE: {rmse:.2f} kg")
print(f"Test R²: {r2:.3f}")

for name, coef in zip(["temp", "humidity", "co2"], model.coef_):
    print(f"coef {name}: {coef:.3f}")
    
joblib.dump(model, "models/linear_regression.joblib")



import json

metrics = {
    "MAE": float(mae),
    "RMSE": float(rmse),
    "R2": float(r2)
}

with open("reports/metrics_linear.json", "w") as f:
    json.dump(metrics, f, indent=4)

    
    
import matplotlib.pyplot as plt
import numpy as np

# pred_test, y_test from Day 9
residuals = y_test - pred_test

fig, axes = plt.subplots(1, 2, figsize=(10, 4))
axes[0].scatter(pred_test, residuals, alpha=0.5)
axes[0].axhline(0, color="red", linestyle="--")
axes[0].set(xlabel="Predicted yield (kg)", ylabel="Residual (kg)")

axes[1].scatter(X_test[:, 1], residuals, alpha=0.5)  # humidity feature column
axes[1].axhline(0, color="red", linestyle="--")
axes[1].set(xlabel="Scaled humidity", ylabel="Residual (kg)")

plt.tight_layout()
plt.savefig("reports/figures/residuals_linear.png", dpi=150)