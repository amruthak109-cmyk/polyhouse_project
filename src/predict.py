import json
import joblib
import streamlit as st
from pathlib import Path

MODEL_DIR = Path("models")

# Load feature names
_feature_cols = json.loads(
    (MODEL_DIR / "feature_cols.json").read_text()
)

# Load scaler and champion model only once
@st.cache_resource
def load_artifacts():
    scaler = joblib.load(MODEL_DIR / "scaler.joblib")
    model = joblib.load(MODEL_DIR / "champion.joblib")
    return scaler, model

_scaler, _model = load_artifacts()


def predict_yield(
    temperature_c: float,
    humidity_pct: float,
    co2_ppm: float
) -> float:

    # Create input row
    row = [[
        temperature_c,
        humidity_pct,
        co2_ppm
    ]]

    # Scale input using the saved scaler
    row_scaled = _scaler.transform(row)

    # Predict yield
    prediction = _model.predict(row_scaled)

    return float(prediction[0])


if __name__ == "__main__":
    result = predict_yield(22.0, 88.0, 920)
    print("Predicted Yield:", round(result, 2), "kg")