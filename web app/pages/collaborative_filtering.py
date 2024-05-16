import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import pickle
import joblib

# Function to preprocess the data and train the model
def preprocess_and_train_model(df):
    # Label encode categorical variables
    label_encoder = LabelEncoder()
    df['Gender'] = label_encoder.fit_transform(df['Gender'])
    df['Location'] = label_encoder.fit_transform(df['Location'])
    df['Interests'] = label_encoder.fit_transform(df['Interests'])
    df['Product_Category_Preference'] = label_encoder.fit_transform(df['Product_Category_Preference'])
    
    # Define features and target variable
    X = df[['Age', 'Gender', 'Location', 'Income', 'Interests', 'Last_Login_Days_Ago',
            'Purchase_Frequency', 'Average_Order_Value', 'Total_Spending',
            'Product_Category_Preference', 'Time_Spent_on_Site_Minutes', 'Pages_Viewed']]
    y = df['Newsletter_Subscription']
    
    # Train a simple RandomForestClassifier
    model = RandomForestClassifier()
    model.fit(X, y)
    
    return model

def load_model(model_path):
    """Loads a model from the specified path using joblib.

    Args:
        model_path (str): Path to the model file.

    Returns:
        object: The loaded model object.
    """
    try:
        model = joblib.load(model_path)
        return model
    except FileNotFoundError:
        print(f"Error: Model file not found at {model_path}")
        return None


if __name__ == "__main__":
    st.title("Newsletter Subscription Prediction")

    model = load_model("kmeans_model.pkl")

    # Get user inputs
    user_id = int(st.number_input("User Id"))
    age = st.slider("Age", min_value=15, max_value=100, value=30)
    gender = st.radio("Gender", ["Male", "Female"])
    location = st.selectbox("Location", ["Urban", "Suburban", "Rural"])
    income = st.number_input("Income", min_value=0, max_value=100000, value=50000)
    interests = st.selectbox("Interests", ["Sports", "Technology", "Fashion", "Travel", "Health & Beauty"])
    last_login_days_ago = st.number_input("Last Login Days Ago", min_value=0, max_value=365, value=7)
    purchase_frequency = st.number_input("Purchase Frequency", min_value=0, value=1)
    avg_order_value = st.number_input("Average Order Value", min_value=0, value=100)
    total_spending = st.number_input("Total Spending", min_value=0, value=1000)
    product_category_preference = st.selectbox("Product Category Preference", ["Books", "Electronics", "Apparel", "Health & Beauty"])
    time_spent_on_site_minutes = st.number_input("Time Spent on Site (Minutes)", min_value=0, value=30)
    pages_viewed = st.number_input("Pages Viewed", min_value=0, value=5)
    newsletter_subscription = st.radio("NewsLetter Subscription" , ["Yes" , "No"])

    if st.button("Predict"):
        # Encode categorical variables
        scaler = joblib.load("min_max_scaler_collaborative.pkl")
        scaled_changes= scaler.transform([[income , total_spending]])
        print(scaled_changes)
        income_scaled = scaled_changes[0][0]
        total_spending_scaled = scaled_changes[0][1]
        gender_encoded = 1 if gender == "Female" else 0
        location_encoded = {"Urban": 0, "Suburban": 1, "Rural": 2}[location]
        interests_encoded = {"Sports": 0, "Technology": 1, "Fashion": 2, "Travel": 3, "Health & Beauty": 4}[interests]
        product_category_preference_encoded = {"Books": 0, "Electronics": 1, "Apparel": 2, "Health & Beauty": 3}[product_category_preference]
        newsletter_subscription_encoded = 1 if newsletter_subscription == "Yes" else 0

        # Make prediction
        user_data = [[user_id , age, gender_encoded, location_encoded, income_scaled, interests_encoded, last_login_days_ago,
                    purchase_frequency, avg_order_value, total_spending_scaled, product_category_preference_encoded,
                    time_spent_on_site_minutes, pages_viewed, newsletter_subscription_encoded]]
        print(user_data)
        prediction = model.predict(user_data)
        st.write("Predicted Newsletter Subscription:", prediction)
        print(prediction)
