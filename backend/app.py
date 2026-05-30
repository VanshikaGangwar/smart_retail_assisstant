from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import logging

from backend.routes.upload import router as upload_router
from backend.routes.forecast import router as forecast_router
from backend.routes.anomaly import router as anomaly_router
from backend.routes.sentiment import router as sentiment_router
from backend.routes.agent import router as agent_router
from backend.routes.upload_blob import router as blob_router
from backend.routes.export_data import router as export_router
from backend.routes.anomaly_check import router as anomaly_check_router


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

app = FastAPI(
    title="Smart Retail Assistant",
    description="AI-powered Smart Retail Assistant Backend",
    version="1.0.0"
)
logger.info("FastAPI app started")

app.include_router(upload_router)
app.include_router(forecast_router)
app.include_router(anomaly_router)
app.include_router(agent_router)
app.include_router(sentiment_router)
app.include_router(blob_router)
app.include_router(export_router)
app.include_router(anomaly_check_router)


@app.get("/", response_class=HTMLResponse)
def home():

    logger.info("Homepage accessed")

    return """
    <!DOCTYPE html>
    <html lang="en">

    <head>

        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <title>Smart Retail Assistant</title>

        <style>

            body{
                margin:0;
                padding:0;
                font-family: Arial, sans-serif;
                background:#f4f4f4;
            }

            .container{
                width:500px;
                margin:100px auto;
                background:white;
                padding:40px;
                border-radius:12px;
                box-shadow:0px 0px 15px rgba(0,0,0,0.1);
                text-align:center;
            }

            h1{
                color:#333;
                margin-bottom:20px;
            }

            p{
                color:#666;
                font-size:18px;
                margin-bottom:30px;
            }

            .btn{
                display:inline-block;
                padding:12px 24px;
                background:#0078ff;
                color:white;
                text-decoration:none;
                border-radius:6px;
                font-size:16px;
                transition:0.3s;
            }

            .btn:hover{
                background:#0056cc;
            }

            .status{
                margin-top:20px;
                color:green;
                font-weight:bold;
            }

        </style>

    </head>

    <body>

        <div class="container">

            <h1>Smart Retail Assistant 🚀</h1>

            <p>
                Backend is Running Successfully
            </p>

            <a class="btn" href="/docs">
                Open Swagger Documentation
            </a>

            <div class="status">
                FastAPI Server Active ✅
            </div>

        </div>

    </body>

    </html>
    """

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):

    logger.error(f"Error occurred: {str(exc)}")

    return {
        "status": "error",
        "message": str(exc)
    }
