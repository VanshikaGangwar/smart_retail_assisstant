from fastapi import FastAPI, Request
import logging

from backend.routes.upload import router as upload_router
from backend.routes.forecast import router as forecast_router
from backend.routes.anomaly import router as anomaly_router
from backend.routes.sentiment import router as sentiment_router
from backend.routes.agent import router as agent_router
from backend.routes.upload_blob import router as blob_router
from backend.routes.export_data import router as export_router

# ---------------- LOGGING ----------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# ---------------- APP ----------------
app = FastAPI(
    title="Smart Retail Assistant"
)

# ---------------- ROUTES ----------------
app.include_router(upload_router)
app.include_router(forecast_router)
app.include_router(anomaly_router)
app.include_router(agent_router)
app.include_router(sentiment_router)
app.include_router(blob_router)
app.include_router(export_router)

# ---------------- HOME ----------------
@app.get("/")
def home():
    logger.info("Home endpoint accessed")
    return {
        "message": "Smart Retail Assistant Running"
    }

# ---------------- GLOBAL ERROR HANDLER ----------------
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Error occurred: {str(exc)}")
    return {
        "status": "error",
        "message": str(exc)
    }

