import streamlit as st
import joblib
import pandas as pd

# Load the trained model
model = joblib.load("models/linear_regression.pkl")

# App title
st.title("EstateIQ - House Price Prediction")

# User inputs
total_sqft = st.number_input("Total Square Feet", min_value=100)
bath = st.number_input("Number of Bathrooms", min_value=1)
balcony = st.number_input("Number of Balconies", min_value=0)
is_ready_to_move = st.selectbox("Ready to Move?", [0, 1])
bhk = st.number_input("BHK", min_value=1)

if st.button("Predict Price"):
    data = pd.DataFrame({
        "total_sqft": [total_sqft],
        "bath": [bath],
        "balcony": [balcony],
        "is_ready_to_move": [is_ready_to_move],
        "BHK": [bhk]
    })

    prediction = model.predict(data)

    st.success(f"Estimated Price: ₹ {prediction[0]:.2f} Lakhs")