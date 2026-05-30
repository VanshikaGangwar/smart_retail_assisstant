from fastapi import APIRouter, UploadFile, File
import pandas as pd

from backend.database.mongodb import sales_collection

import logging
logger = logging.getLogger(__name__)

router = APIRouter()

@router.post("/upload-data")
async def upload_data(file: UploadFile = File(...)):

    logger.info("Upload API called")

    try:
        df = pd.read_csv(file.file)
        logger.info(f"CSV file read successfully with {len(df)} rows")

        data = df.to_dict(orient="records")

        sales_collection.insert_many(data)
        logger.info("Data inserted into MongoDB successfully")

        return {
            "message": "Data uploaded successfully",
            "rows_uploaded": len(data)
        }

    except Exception as e:
        logger.error(f"Error during upload: {str(e)}")

        return {
            "message": "Upload failed",
            "error": str(e)
        }