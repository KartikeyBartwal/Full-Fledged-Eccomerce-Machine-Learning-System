import streamlit as st
import pandas as pd
import numpy as np
from pickle import load  # Assuming you saved your model using pickle

# Title
st.title("Product Price Prediction")

# Price Input
price = st.number_input("Price", min_value=0.0, format="%f")

# Discount Input
discount = st.number_input("Discount", min_value=0.0, format="%f")

# Rating Input
rating = st.slider("Rating", min_value=0.0, max_value=5.0, step=0.1)

# Number of Reviews Input
num_reviews = st.number_input("Number of Reviews", min_value=0)

# Brand Popularity Input
brand_popularity = st.slider("Brand Popularity", min_value=0.0, max_value=1.0, step=0.1)

# Marketing Spend Input
marketing_spend = st.number_input("Marketing Spend", min_value=0.0, format="%f")

# Social Media Followers Input
social_media_followers = st.number_input("Social Media Followers", min_value=0)

# Seasonality Input
seasonality = st.slider("Seasonality", min_value=0.0, max_value=1.0, step=0.1)

# Past 60 Day Sales Input
past_sales = st.number_input("Past 60 Day Sales", min_value=0)

# Percentage Repeating Customers Input
repeating_customers = st.slider("Percentage Repeating Customers", min_value=0.0, max_value=1.0, step=0.01)

# Competition Level Input
competition_level = st.selectbox("Competition Level", ["competitive", "very competitive", "easy", "normal", "healthy", "less"])

# Load Model (Replace with your model loading logic)
def load_model(model_path):
    try:
        with open(model_path, 'rb') as file:
            model = load(file)
            return model
    except FileNotFoundError:
        print(f"Error: Model file not found at {model_path}")
        return None

loaded_model = load_model("next_60_days_sales_estimation.pkl")  # Replace with your model path

competition_level_labels = {
    "competitive": -1,
    "very competitive": -2,
    "easy": 2,
    "normal": 0,
    "healthy": 0,
    "less": 1
}


# Prediction Button and Output
if st.button("Predict Price"):
    if loaded_model is not None:
        # Prepare input data (convert to NumPy array)
        inputs = np.array([price, discount, rating, num_reviews, brand_popularity, marketing_spend,
                           social_media_followers, seasonality, past_sales, repeating_customers,
                           competition_level_labels[competition_level]])

        # Make prediction
        predicted_price = loaded_model.predict([inputs])[0]  # Assuming single output
        # Display predicted price with two decimal places and green font color
        st.write(f"Estmated sales in the next 60 days: {int(predicted_price)}", style="color: green; font-weight: bold;")
    else:
        st.warning("Error: Model could not be loaded.")
