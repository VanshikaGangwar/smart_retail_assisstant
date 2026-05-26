from fastapi import APIRouter, UploadFile, File
import pandas as pd

from backend.database.mongodb import sales_collection

router = APIRouter()

@router.post("/upload-data")
async def upload_data(file: UploadFile = File(...)):

    df = pd.read_csv(file.file)

    data = df.to_dict(orient="records")

    sales_collection.insert_many(data)

    return {
        "message": "Data uploaded successfully",
        "rows_uploaded": len(data)
    }