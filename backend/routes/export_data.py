from fastapi import APIRouter

import pandas as pd

router = APIRouter()

@router.get("/export-sales-data")

def export_sales_data():

    df = pd.read_csv("data/sales.csv")

    export_path = "data/powerbi_sales.csv"

    df.to_csv(export_path, index=False)

    return {
        "message": "Data exported successfully",
        "file": export_path
    }