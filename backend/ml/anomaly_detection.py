import pandas as pd
from sklearn.ensemble import IsolationForest

# Load dataset
df = pd.read_csv("data/sales.csv")

# Convert date column
df['Date'] = pd.to_datetime(
    df['Date'],
    dayfirst=True,
    errors='coerce'
)

# Remove invalid rows
df.dropna(inplace=True)

# Features for anomaly detection
features = df[['Weekly_Sales']]

# Isolation Forest Model
model = IsolationForest(
    n_estimators=100,
    contamination=0.02,
    random_state=42
)

# Train model
model.fit(features)

# Predict anomalies
df['Anomaly'] = model.predict(features)

# Convert:
# -1 = anomaly
# 1 = normal

df['Anomaly'] = df['Anomaly'].map({
    1: "Normal",
    -1: "Anomaly"
})

# Get anomalies only
anomalies = df[df['Anomaly'] == "Anomaly"]

def get_anomalies():

    results = anomalies[
        ['Date', 'Store', 'Weekly_Sales', 'Anomaly']
    ]

    return results.to_dict(orient='records')

def check_single_sale(weekly_sales: float):

    # Create dataframe like training
    data = pd.DataFrame([{
        "Weekly_Sales": weekly_sales
    }])

    # Use SAME trained model
    prediction = model.predict(data)[0]

    if prediction == -1:
        return "Anomaly"
    else:
        return "Normal"