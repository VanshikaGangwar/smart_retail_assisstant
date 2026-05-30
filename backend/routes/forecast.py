from fastapi import APIRouter
from backend.ml.predict import predict_sales

import logging
logger = logging.getLogger(__name__)

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

    logger.info("Forecast API called")

    try:
        logger.info(f"Input received: Store={store}, Temp={temperature}, CPI={cpi}")

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

        logger.info(f"Prediction generated: {prediction}")

        return {
            "predicted_sales": round(prediction, 2)
        }

    except Exception as e:
        logger.error(f"Forecast error: {str(e)}")

        return {
            "message": "Prediction failed",
            "error": str(e)
        }