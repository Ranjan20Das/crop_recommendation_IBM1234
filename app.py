import streamlit as st
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# ------------------------------
# Page Config
# ------------------------------
st.set_page_config(
    page_title="Crop Recommendation System",
    page_icon="🌱",
    layout="centered"
)

st.title("🌾 Crop Recommendation System")
st.write("Enter soil and climate details to get the best crop recommendation.")

# ------------------------------
# Load Dataset
# ------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("Crop_recommendation.csv")
    return df

df = load_data()

# ------------------------------
# Train Model
# ------------------------------
@st.cache_resource
def train_model(df):
    X = df.drop("label", axis=1)
    y = df["label"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier(
        n_estimators=200,
        random_state=42
    )

    model.fit(X_train, y_train)
    return model

model = train_model(df)

# ------------------------------
# User Inputs
# ------------------------------
st.subheader("🌱 Input Parameters")

col1, col2 = st.columns(2)

with col1:
    N = st.number_input("Nitrogen (N)", min_value=0.0)
    P = st.number_input("Phosphorus (P)", min_value=0.0)
    K = st.number_input("Potassium (K)", min_value=0.0)
    temperature = st.number_input("Temperature (°C)", min_value=0.0)

with col2:
    humidity = st.number_input("Humidity (%)", min_value=0.0)
    ph = st.number_input("pH Value", min_value=0.0, max_value=14.0)
    rainfall = st.number_input("Rainfall (mm)", min_value=0.0)

# ------------------------------
# Prediction
# ------------------------------
if st.button("🌾 Recommend Crop"):
    input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    prediction = model.predict(input_data)[0]

    st.success(f"✅ Recommended Crop: **{prediction.upper()}**")
