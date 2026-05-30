from fastapi import APIRouter

from backend.ml.anomaly_detection import check_single_sale

router = APIRouter()


@router.get("/check-anomaly")
def check_anomaly(weekly_sales: float):

    result = check_single_sale(weekly_sales)

    return {
        "input_sales": weekly_sales,
        "prediction": result
    }