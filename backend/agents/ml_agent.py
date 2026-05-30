def ml_agent(question):

    # normalize input properly
    question = question.lower().strip()

    # MODEL INFO
    if "model" in question or "algorithm" in question:

        return """
Machine Learning Models Used:

1. Random Forest Regressor → Sales Forecasting
2. Isolation Forest → Anomaly Detection
"""

    # FEATURE ENGINEERING
    elif "feature" in question or "engineering" in question:

        return """
Feature Engineering includes:

- Handling missing values
- Selecting important features (Store, CPI, Fuel Price, etc.)
- Encoding categorical variables
- Scaling numerical values
- Removing noise/outliers

It improves model accuracy and stability.
"""

    # PREDICTION
    elif "predict" in question or "forecast" in question:

        return """
Sales prediction is done using Random Forest.

It uses:
- Store
- Temperature
- Fuel Price
- CPI
- Unemployment
"""

    # ANOMALY DETECTION
    elif "anomaly" in question or "outlier" in question:

        return """
Isolation Forest detects abnormal patterns like:

- Sudden spikes in sales
- Unexpected drops
- Fraud-like behavior
"""

    # DEFAULT
    else:

        return """
Ask questions like:
- What models are used?
- Explain feature engineering
- How prediction works?
- What is anomaly detection?
"""