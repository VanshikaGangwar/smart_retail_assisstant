import pandas as pd
import numpy as np
import pickle
import os

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score



# Read CSV file

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

file_path = os.path.join(BASE_DIR, "data", "sales.csv")

print("Reading from:", file_path)

df = pd.read_csv(file_path)

print("Dataset Loaded Successfully")
print(df.head())

# DATA CLEANING
# Convert Date column


df['Date'] = pd.to_datetime(
    df['Date'],
    dayfirst=True,
    errors='coerce'
)

# Remove invalid dates

df.dropna(subset=['Date'], inplace=True)

# Remove duplicate rows

df.drop_duplicates(inplace=True)

# Remove missing values if any

df.dropna(inplace=True)

# FEATURE ENGINEERING
# Extract date features

df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day
df['Week'] = df['Date'].dt.isocalendar().week.astype(int)

# REMOVE OUTLIERS

# Remove extreme sales values
# Helps reduce MAE significantly

Q1 = df['Weekly_Sales'].quantile(0.25)
Q3 = df['Weekly_Sales'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Keep only normal sales values

df = df[
    (df['Weekly_Sales'] >= lower_bound) &
    (df['Weekly_Sales'] <= upper_bound)
]

print("Outliers Removed")

# Important retail forecasting features

features = [
    'Store',
    'Holiday_Flag',
    'Temperature',
    'Fuel_Price',
    'CPI',
    'Unemployment',
    'Year',
    'Month',
    'Day',
    'Week'
]

X = df[features]
y = df['Weekly_Sales']

# TRAIN TEST SPLIT

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# RANDOM FOREST MODEL

model = RandomForestRegressor(
    n_estimators=300,
    max_depth=20,
    min_samples_split=5,
    min_samples_leaf=2,
    random_state=42,
    n_jobs=-1
)

# TRAIN MODEL

print("Training Model...")

model.fit(X_train, y_train)

print("Model Training Completed")

# PREDICTIONS

predictions = model.predict(X_test)

# EVALUATION

mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("\n===== MODEL EVALUATION =====")
print(f"Mean Absolute Error (MAE): {mae:.2f}")
print(f"R2 Score: {r2:.4f}")

# SAVE MODEL

model_path = os.path.join(BASE_DIR, "backend", "saved_models", "forecast_model.pkl")

# Create folder if not exists
os.makedirs(os.path.dirname(model_path), exist_ok=True)

with open(model_path, "wb") as f:
    pickle.dump(model, f)

print("\nModel Saved Successfully")
print("Location:", model_path)