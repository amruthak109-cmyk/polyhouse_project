import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from predict import predict_yield


def test_predict_returns_float():
    result = predict_yield(22.0, 88.0, 920)
    assert isinstance(result, float)


def test_prediction_in_range():
    result = predict_yield(22.0, 88.0, 920)
    assert 0 < result < 50


def test_prediction_changes():
    low = predict_yield(10.0, 50.0, 400)
    high = predict_yield(35.0, 100.0, 2000)
    assert low != high