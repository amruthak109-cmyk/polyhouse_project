import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from joblib import load

# Load test data
X_test = np.load("data/processed/X_test.npy")
y_test = np.load("data/processed/y_test.npy")

# Load champion model
champion = load("models/champion.joblib")

# Predict
pred = champion.predict(X_test)

# Model comparison table
results = pd.DataFrame({
    "Model": ["Linear Regression", "Random Forest", "Tuned Random Forest"],
    "Test MAE": [0.42, 0.48, 0.467],   # replace if your values differ
    "Test R²": [0.427, 0.31, 0.312]    # replace if your values differ
})

print(results.to_markdown(index=False))

# Predicted vs Actual Plot
plt.figure(figsize=(6, 6))
plt.scatter(y_test, pred, alpha=0.6)

plt.plot(
    [y_test.min(), y_test.max()],
    [y_test.min(), y_test.max()],
    "r--"
)

plt.xlabel("Actual Yield (kg)")
plt.ylabel("Predicted Yield (kg)")
plt.title("Champion Model: Predicted vs Actual")

plt.tight_layout()
plt.savefig("reports/figures/pred_vs_actual.png", dpi=150)

print("\nSaved: reports/figures/pred_vs_actual.png")