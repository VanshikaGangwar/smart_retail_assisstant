from fastapi import APIRouter
from backend.ml.anomaly_detection import get_anomalies

import logging
logger = logging.getLogger(__name__)

router = APIRouter()

@router.get("/detect-anomalies")
def detect_anomalies():

    logger.info("Anomaly Detection API called")

    try:
        results = get_anomalies()

        logger.info(f"Total anomalies detected: {len(results)}")

        return {
            "total_anomalies": len(results),
            "anomalies": results[:]
        }

    except Exception as e:
        logger.error(f"Anomaly detection failed: {str(e)}")

        return {
            "message": "Anomaly detection failed",
            "error": str(e)
        }