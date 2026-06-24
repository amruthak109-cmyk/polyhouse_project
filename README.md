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
- Training rows: 288
- Testing rows: 72
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

## Task 7: Hyperparameter Tuning, Model Comparison & Metric Selection

GridSearchCV with TimeSeriesSplit cross-validation was used to tune the Random Forest model. The best hyperparameters obtained were max_depth = 8, min_samples_leaf = 5, and n_estimators = 100. The tuned model achieved a CV MAE of 0.463, a Test MAE of 0.467, and a Test R² of 0.312.

### Model Comparison

| Model               | Test MAE | Test R² |
| ------------------- | -------- | ------- |
| Linear Regression   | 0.42     | 0.427   |
| Random Forest       | 0.48     | 0.31    |
| Tuned Random Forest | 0.467    | 0.312   |

### Champion Model

Linear Regression was selected as the champion model because it achieved the lowest test MAE and demonstrated more stable performance during cross-validation compared to both Random Forest models.

### Saved Artifacts

* models/rf_best_params.json
* models/champion.joblib
* reports/figures/pred_vs_actual.png

### Limitations

* The dataset covers a limited time period.
* Sensor readings may contain noise and measurement errors.
* Model performance may vary across different seasons.
* Predictions may be less reliable outside the observed sensor ranges.
## Model Persistence & Reproducibility

A prediction script was created to load the saved champion model and generate mushroom yield predictions from new sensor readings. The predict_yield() function uses temperature, humidity, and CO₂ values as input and returns the predicted yield. Feature order was maintained using feature_cols.json to ensure consistency between training and inference. The model was successfully loaded without retraining and produced a sample prediction of 17.96 kg.

Saved Artifacts:

* models/champion.joblib
* models/feature_cols.json
* src/predict.py
## Task 8: Streamlit Yield Forecast App

A Streamlit web application was developed to predict oyster mushroom yield using environmental sensor readings.

Features:
- Sidebar sliders for Temperature, Humidity and CO₂
- Champion model loaded for prediction
- Predict Yield button
- Estimated daily yield displayed in kilograms

Run the app:

streamlit run src/app.py

## Task 9: Cloud Deployment & Monitoring

The Mushroom Yield Forecast application was prepared for cloud deployment using Streamlit Community Cloud. All required Python dependencies were listed in `requirements.txt` to ensure reproducible deployment. Prediction logging was integrated into the application to record each prediction for future monitoring and analysis.

### Monitoring

Prediction logs are stored in:

* `logs/predictions.csv`

Each prediction record contains:

* Timestamp (UTC)
* Temperature (°C)
* Humidity (%)
* CO₂ (ppm)
* Predicted Yield (kg)

A monitoring plan was documented to identify data drift and determine when model retraining is required.

### Deployment Files

* `requirements.txt`
* `src/app.py`
* `src/logger.py`
* `docs/monitoring.md`

---

## Task 10: Technical Report & Capstone Presentation

A complete technical report and capstone presentation were prepared to summarize the entire machine learning pipeline developed during the internship.

The report includes:

* Problem statement
* Dataset description
* Data cleaning and preprocessing
* Exploratory Data Analysis (EDA)
* Feature engineering
* Model development and evaluation
* Streamlit application
* Cloud deployment
* Monitoring strategy
* Limitations and future work

Presentation slides were also created to demonstrate the complete workflow, model results, deployment, and project outcomes.

### Final Deliverables

* `reports/final_report.md`
* Presentation (`.pptx`)
* GitHub Repository
* Streamlit Deployment
* Project Documentation