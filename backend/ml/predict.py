import pickle
import pandas as pd

# Load trained model
with open("backend/saved_models/forecast_model.pkl", "rb") as f:
    model = pickle.load(f)

def predict_sales(
    store,
    holiday_flag,
    temperature,
    fuel_price,
    cpi,
    unemployment,
    year,
    month,
    day,
    week
):

    # Create dataframe with SAME feature names
    features = pd.DataFrame([{
        "Store": store,
        "Holiday_Flag": holiday_flag,
        "Temperature": temperature,
        "Fuel_Price": fuel_price,
        "CPI": cpi,
        "Unemployment": unemployment,
        "Year": year,
        "Month": month,
        "Day": day,
        "Week": week
    }])

    # Prediction
    prediction = model.predict(features)

    return prediction[0]