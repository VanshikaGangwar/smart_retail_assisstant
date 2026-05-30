from fastapi import APIRouter
import pandas as pd
import os

router = APIRouter()

@router.get("/export-sales-data")
def export_sales_data():

    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

    input_path = os.path.join(BASE_DIR, "data", "sales.csv")
    output_path = os.path.join(BASE_DIR, "data", "powerbi_sales.csv")

    df = pd.read_csv(input_path)

    # DATA CLEANING
    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)

    # FEATURE ENGINEERING
    df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month
    df['Week'] = df['Date'].dt.isocalendar().week.astype(int)

    # SAVE CLEAN DATA
    df.to_csv(output_path, index=False)

    return {
        "message": "Data cleaned & exported successfully",
        "file": output_path,
        "rows": len(df)
    }