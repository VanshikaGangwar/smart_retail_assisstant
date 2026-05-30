from fastapi import APIRouter

from backend.azure.sentiment import analyze_sentiment

router = APIRouter()

@router.get("/analyze-sentiment")
def sentiment(text: str):

    result = analyze_sentiment(text)

    return result