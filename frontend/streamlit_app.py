import streamlit as st
import requests

st.set_page_config(
    page_title="Smart Retail Assistant",
    layout="centered"
)

st.title("🛒 Smart Retail Assistant")

st.subheader("Demand Forecasting System")

# Inputs

store = st.number_input("Store", value=1)

holiday_flag = st.selectbox(
    "Holiday Flag",
    [0, 1]
)

temperature = st.number_input(
    "Temperature",
    value=42.0
)

fuel_price = st.number_input(
    "Fuel Price",
    value=3.5
)

cpi = st.number_input(
    "CPI",
    value=210.0
)

unemployment = st.number_input(
    "Unemployment",
    value=8.1
)

year = st.number_input(
    "Year",
    value=2026
)

month = st.number_input(
    "Month",
    value=8
)

day = st.number_input(
    "Day",
    value=15
)

week = st.number_input(
    "Week",
    value=33
)

# Predict Button

if st.button("Predict Sales"):

    url = (
        "http://127.0.0.1:8000/predict-demand"
        f"?store={store}"
        f"&holiday_flag={holiday_flag}"
        f"&temperature={temperature}"
        f"&fuel_price={fuel_price}"
        f"&cpi={cpi}"
        f"&unemployment={unemployment}"
        f"&year={year}"
        f"&month={month}"
        f"&day={day}"
        f"&week={week}"
    )

    response = requests.get(url)

    result = response.json()

    st.success(
        f"Predicted Sales: {result['predicted_sales']}"
    )

st.subheader("Sales Anomaly Detection")

if st.button("Detect Anomalies"):

    response = requests.get(
        "http://127.0.0.1:8000/detect-anomalies"
    )

    result = response.json()

    st.warning(
        f"Total Anomalies Found: {result['total_anomalies']}"
    )

    st.write(result['anomalies'])    