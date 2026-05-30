import os

from dotenv import load_dotenv
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

# Load env variables
load_dotenv()

_client = None


def get_text_analytics_client():
    global _client

    if _client is None:
        key = os.getenv("AZURE_LANGUAGE_KEY")
        endpoint = os.getenv("AZURE_LANGUAGE_ENDPOINT")

        if not key or not endpoint:
            raise RuntimeError(
                "AZURE_LANGUAGE_KEY and AZURE_LANGUAGE_ENDPOINT must be configured"
            )

        _client = TextAnalyticsClient(
            endpoint=endpoint,
            credential=AzureKeyCredential(key)
        )

    return _client

def analyze_sentiment(text):

    response = get_text_analytics_client().analyze_sentiment(
        documents=[text]
    )[0]

    return {
        "sentiment": response.sentiment,
        "positive_score": response.confidence_scores.positive,
        "neutral_score": response.confidence_scores.neutral,
        "negative_score": response.confidence_scores.negative
    }
