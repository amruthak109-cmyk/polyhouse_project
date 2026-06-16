import json
import joblib
from pathlib import Path

MODEL_DIR = Path("models")

# Load champion model
_model = joblib.load(MODEL_DIR / "champion.joblib")

# Load feature order
_feature_cols = json.loads(
    (MODEL_DIR / "feature_cols.json").read_text()
)

def predict_yield(
    temperature_c: float,
    humidity_pct: float,
    co2_ppm: float
) -> float:

    row = [[
        temperature_c,
        humidity_pct,
        co2_ppm
    ]]

    prediction = _model.predict(row)

    return float(prediction[0])

if __name__ == "__main__":
    result = predict_yield(22.0, 88.0, 920)
    print("Predicted Yield:", round(result, 2), "kg")