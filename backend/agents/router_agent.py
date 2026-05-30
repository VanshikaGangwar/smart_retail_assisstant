from backend.agents.document_agent import document_agent
from backend.agents.analytics_agent import analytics_agent
from backend.agents.ml_agent import ml_agent

def router_agent(question):

    q = question.lower()

    # Document Agent
    if any(word in q for word in [
        "policy",
        "return",
        "faq",
        "offer",
        "discount"
    ]):

        return document_agent(question)

    # Analytics Agent
    elif any(word in q for word in [
        "sales",
        "store",
        "analytics",
        "revenue"
    ]):

        return analytics_agent(question)

    # ML Agent
    elif any(word in q for word in [
        "forecast",
        "prediction",
        "anomaly",
        "model"
    ]):

        return ml_agent(question)

    else:

        return """
        Ask about:
        - retail policies
        - analytics
        - forecasting
        - anomalies
        """