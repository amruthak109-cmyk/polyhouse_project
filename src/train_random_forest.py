from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import joblib
import matplotlib.pyplot as plt

import numpy as np

X_train = np.load("data/processed/X_train.npy")
X_test = np.load("data/processed/X_test.npy")
y_train = np.load("data/processed/y_train.npy")
y_test = np.load("data/processed/y_test.npy")

rf = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)
rf.fit(X_train, y_train)

pred = rf.predict(X_test)
print(f"RF Test MAE: {mean_absolute_error(y_test, pred):.2f} kg")
print(f"RF Test R²:  {r2_score(y_test, pred):.3f}")
train_pred = rf.predict(X_train)

train_mae = mean_absolute_error(y_train, train_pred)
test_mae = mean_absolute_error(y_test, pred)

print(f"Train MAE: {train_mae:.2f} kg")
print(f"Test MAE:  {test_mae:.2f} kg")

importances = rf.feature_importances_
labels = ["temperature", "humidity", "co2"]
plt.barh(labels, importances)
plt.xlabel("Importance")
plt.title("Random Forest Feature Importance")
plt.tight_layout()
plt.savefig("reports/figures/rf_importance.png", dpi=150)

joblib.dump(rf, "models/random_forest.joblib")