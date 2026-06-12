coloumns:

timestamp - Date and time of sensor reading
temperature_c - Temperature in Celsius
humidity_pct - Humidity percentage
co2_ppm - CO₂ concentration in ppm
yield_kg - Mushroom yield in kilograms

Task 4: Feature Engineering & Temporal Train/Test Split

Features:
- temperature_c
- humidity_pct
- co2_ppm

Train/Test Split:
- Training rows: XXX
- Testing rows: XXX
- Train period: 2024-01-01 to 2024-10-18
- Test period: 2024-10-19 to 2024-12-30

Scaling:
- MinMaxScaler used
- Fitted on training data only
- Test data transformed using training statistics

Saved Artifact:
- models/scaler.joblib


## Task 5: Baseline Linear Regression Model

A Linear Regression model was trained using temperature, humidity, and CO₂ sensor data to predict mushroom yield. The model was evaluated on the test dataset using MAE, RMSE, and R² metrics.

### Test Metrics

* MAE: 0.42 kg
* RMSE: 0.54 kg
* R²: 0.427

### Coefficient Interpretation

* Temperature coefficient: 1.894 (positive impact on yield)
* Humidity coefficient: 0.959 (positive impact on yield)
* CO₂ coefficient: -1.213 (negative impact on yield)

### Baseline Evaluation

The model achieved an R² score of 0.427, indicating that it explains approximately 42.7% of the variation in mushroom yield. While the performance is moderate, it serves as a useful baseline for comparing more advanced machine learning models in future tasks.

### Saved Artifacts

* Model: `models/linear_regression.joblib`
* Metrics: `reports/metrics_linear.json`