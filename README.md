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