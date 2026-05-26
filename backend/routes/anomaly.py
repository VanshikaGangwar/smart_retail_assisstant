from fastapi import APIRouter

from backend.ml.anomaly_detection import get_anomalies

router = APIRouter()

@router.get("/detect-anomalies")
def detect_anomalies():

    results = get_anomalies()

    return {
        "total_anomalies": len(results),
        "anomalies": results[:10]
    }