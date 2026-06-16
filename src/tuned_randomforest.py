import numpy as np
import json
import joblib

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV, TimeSeriesSplit
from sklearn.metrics import mean_absolute_error, r2_score

X_train = np.load("data/processed/X_train.npy")
X_test = np.load("data/processed/X_test.npy")
y_train = np.load("data/processed/y_train.npy")
y_test = np.load("data/processed/y_test.npy")

tscv = TimeSeriesSplit(n_splits=3)

param_grid = {
    "n_estimators": [50, 100, 200],
    "max_depth": [None, 8, 16],
    "min_samples_leaf": [1, 3, 5]
}

rf = RandomForestRegressor(random_state=42)

search = GridSearchCV(
    rf,
    param_grid,
    cv=tscv,
    scoring="neg_mean_absolute_error"
)

search.fit(X_train, y_train)

print("Best params:", search.best_params_)
print("Best CV MAE:", -search.best_score_)

best_model = search.best_estimator_

pred = best_model.predict(X_test)

print("Test MAE:", mean_absolute_error(y_test, pred))
print("Test R²:", r2_score(y_test, pred))

with open("models/rf_best_params.json", "w") as f:
    json.dump(search.best_params_, f, indent=2)

joblib.dump(best_model, "models/champion.joblib")