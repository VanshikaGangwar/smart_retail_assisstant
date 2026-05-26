import os

from dotenv import load_dotenv

from azure.ai.textanalytics import TextAnalyticsClient

from azure.core.credentials import AzureKeyCredential

# Load env variables
load_dotenv()

KEY = os.getenv("AZURE_LANGUAGE_KEY")

ENDPOINT = os.getenv("AZURE_LANGUAGE_ENDPOINT")

# Azure Client
client = TextAnalyticsClient(
    endpoint=ENDPOINT,
    credential=AzureKeyCredential(KEY)
)

def analyze_sentiment(text):

    response = client.analyze_sentiment(
        documents=[text]
    )[0]

    return {
        "sentiment": response.sentiment,
        "positive_score": response.confidence_scores.positive,
        "neutral_score": response.confidence_scores.neutral,
        "negative_score": response.confidence_scores.negative
    }