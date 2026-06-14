colums :
timestamp - Date and time of sensor reading
temperature_c - Temperature in Celsius
humidity_pct - Humidity percentage
co2_ppm - CO₂ concentration in ppm
yield_kg - Mushroom yield in kilograms

## Task 4: Feature Engineering & Temporal Train/Test Split

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

Saved Models in:
- models/scaler.joblib

## Task 5: Baseline Linear Regression Model

A Linear Regression model was trained using temperature, humidity, and CO₂ sensor data to predict mushroom yield. The model was evaluated on the test dataset using MAE, RMSE, and R² metrics.

 Test Metrics

* MAE: 0.42 kg
* RMSE: 0.54 kg
* R²: 0.427

Coefficient Interpretation

* Temperature coefficient: 1.894 (positive impact on yield)
* Humidity coefficient: 0.959 (positive impact on yield)
* CO₂ coefficient: -1.213 (negative impact on yield)

 Baseline Evaluation

The model achieved an R² score of 0.427, indicating that it explains approximately 42.7% of the variation in mushroom yield. While the performance is moderate, it serves as a useful baseline for comparing more advanced machine learning models in future tasks.

 Saved Artifacts

* Model: `models/linear_regression.joblib`
* Metrics: `reports/metrics_linear.json`

Residual analysis was performed to evaluate the prediction errors of the Linear Regression model.

Residuals were calculated as:

Residual = Actual Yield − Predicted Yield

Diagnostic Plots
Residual vs Predicted Yield
Residual vs Humidity
Observations
Residuals were distributed around zero.
No strong systematic pattern was observed.
The Linear Regression model provides a reasonable baseline prediction.
Saved Figure
reports/figures/residuals_linear.png

## Task 6: Random Forest Model

A Random Forest Regressor was trained using temperature, humidity, and CO₂ features to capture non-linear relationships in the data.

Feature Importance

The feature importance analysis showed:

Temperature – Highest importance
CO₂ – Second highest importance
Humidity – Lowest importance

This indicates that temperature contributes the most to mushroom yield prediction in the Random Forest model.

Saved Artifacts
models/random_forest.joblib
reports/figures/rf_importance.png

##Cross Validation & Overfitting Analysis

TimeSeriesSplit cross-validation with 5 folds was used to evaluate model performance while preserving the temporal nature of the dataset.

Cross Validation Results
Random Forest CV MAE: 0.487 ± 0.032
Linear Regression CV MAE: 0.450 ± 0.026
Observations
Linear Regression achieved a lower average MAE than Random Forest.
Linear Regression showed lower variation across folds.
No test data was used during cross-validation.
TimeSeriesSplit preserved chronological order and prevented data leakage.