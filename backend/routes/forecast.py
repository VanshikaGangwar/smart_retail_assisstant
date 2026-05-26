from fastapi import APIRouter

from backend.ml.predict import predict_sales

router = APIRouter()

@router.get("/predict-demand")
def forecast(
    store: int,
    holiday_flag: int,
    temperature: float,
    fuel_price: float,
    cpi: float,
    unemployment: float,
    year: int,
    month: int,
    day: int,
    week: int
):

    prediction = predict_sales(
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
    )

    return {
        "predicted_sales": round(prediction, 2)
    }