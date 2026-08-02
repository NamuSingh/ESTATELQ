import streamlit as st
import joblib
import pandas as pd

# ==========================================
# PAGE CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="EstateIQ",
    page_icon="🏠",
    layout="wide"
)

# ==========================================
# LOAD TRAINED MODEL
# ==========================================
model = joblib.load("models/linear_regression.pkl")

# ==========================================
# MAIN TITLE
# ==========================================
st.title("🏠 EstateIQ")
st.subheader("AI-Powered House Price Prediction")

st.info(
    "Welcome to EstateIQ! Enter the property details from the sidebar and click Predict Price."
)

# ==========================================
# SIDEBAR
# ==========================================
st.sidebar.title("🏡 Property Details")

total_sqft = st.sidebar.number_input(
    "Total Square Feet",
    min_value=300,
    max_value=10000,
    value=1200
)

bath = st.sidebar.number_input(
    "Bathrooms",
    min_value=1,
    max_value=10,
    value=2
)

balcony = st.sidebar.number_input(
    "Balconies",
    min_value=0,
    max_value=5,
    value=1
)

ready = st.sidebar.selectbox(
    "Ready to Move",
    ["Yes", "No"]
)

bhk = st.sidebar.number_input(
    "BHK",
    min_value=1,
    max_value=10,
    value=2
)

# Convert Yes/No into 1/0
is_ready_to_move = 1 if ready == "Yes" else 0

# ==========================================
# PREDICTION
# ==========================================
if st.button("🔍 Predict Price"):

    input_data = pd.DataFrame({
        "total_sqft": [total_sqft],
        "bath": [bath],
        "balcony": [balcony],
        "is_ready_to_move": [is_ready_to_move],
        "BHK": [bhk]
    })

    prediction = model.predict(input_data)

    price = round(prediction[0], 2)

    st.success("Prediction Completed Successfully!")

    st.metric(
        label="🏠 Estimated House Price",
        value=f"₹ {price:.2f} Lakhs"
    )

    st.balloons()

# ==========================================
# ABOUT SECTION
# ==========================================
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.header("📌 About EstateIQ")

    st.write("""
EstateIQ is an AI-powered House Price Prediction System.

It predicts Bengaluru house prices using Machine Learning algorithms.
""")

with col2:
    st.header("🛠 Technologies Used")

    st.write("""
- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Joblib
""")

# ==========================================
# FEATURES
# ==========================================
st.markdown("---")

st.header("✨ Features")

st.markdown("""
- 🏠 House Price Prediction
- 📐 Total Square Feet
- 🚿 Bathrooms
- 🌇 Balconies
- 🏡 Ready to Move
- 🛏 BHK Prediction
- ⚡ Fast Prediction
- 🤖 Machine Learning Model
""")

# ==========================================
# FOOTER
# ==========================================
st.markdown("---")

st.caption("© 2026 EstateIQ | Developed by Aarohi Singh")