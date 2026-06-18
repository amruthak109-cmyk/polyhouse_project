import streamlit as st
from predict import predict_yield

st.set_page_config(
    page_title="Mushroom Yield Forecast",
    layout="centered"
)

st.title("🍄 Polyhouse Yield Predictor")

st.caption(
    "Predict oyster mushroom yield using environmental sensor readings"
)

# Sidebar Inputs
with st.sidebar:

    st.header("Sensor Readings")

    temp = st.slider(
        "Temperature (°C)",
        min_value=10.0,
        max_value=35.0,
        value=22.0,
        step=0.1
    )

    humid = st.slider(
        "Humidity (%)",
        min_value=50.0,
        max_value=100.0,
        value=85.0,
        step=0.5
    )

    co2 = st.slider(
        "CO₂ (ppm)",
        min_value=400,
        max_value=2000,
        value=900,
        step=10
    )
st.write("Temperature:", temp)
st.write("Humidity:", humid)
st.write("CO2:", co2)
if st.button("Predict Yield"):

    prediction = predict_yield(
        temp,
        humid,
        co2
    )

    st.metric(
        label="Estimated Daily Yield",
        value=f"{prediction:.2f} kg"
    )