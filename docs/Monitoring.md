# Monitoring Plan

## Prediction Logging

* Every prediction is saved in `logs/predictions.csv`.
* The log stores timestamp, temperature, humidity, CO₂, and predicted yield.

## Model Monitoring

* Check prediction logs regularly for unusual values.
* Compare predictions with actual yield when available.

## Retraining Triggers

* Retrain the model if prediction accuracy decreases.
* Retrain when new sensor data is collected.

## Future Improvements

1. Collect more polyhouse sensor data.
2. Retrain the model periodically.
3. Improve the Streamlit app with graphs and analytics.