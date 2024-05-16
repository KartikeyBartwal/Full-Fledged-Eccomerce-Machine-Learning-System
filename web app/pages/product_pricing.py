import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Stunning Background Image
page_bg_img = '''
<style>
body {
  background-image: url("https://images.unsplash.com/photo-1504753793650-d43f7acd8b83?fit=crop&w=1920&h=1080");
  background-size: cover;
  background-attachment: fixed;
  font-family: sans-serif;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

# Informative Title
st.title("Smart Product Recommendation Engine")

# User Input Section with Dropdowns
st.header("Provide Product Information")

# Feature dropdowns with pre-defined options
color_options = ["Black", "White", "Silver", "Blue", "Green", "Red", "RGB", "Brown", "Beige"]
color_selected = st.selectbox("Color", color_options)

material_options = ["Plastic", "Metal", "Wood", "Fabric", "Nylon", "Aluminum", "Glass", "Stainless Steel", "Leather", "Paper", "Foam"]
material_selected = st.selectbox("Material", material_options)

category_options = ["Home & Office", "Kitchen Appliances", "Audio Devices", "Computer Accessories", "Car Accessories", "Outdoor & Sports", "Home Security", 
                   "Home Appliances", "Health & Wellness", "Apparel & Accessories", "Home Automation", "Mobile Accessories", "Pet Supplies", 
                   "Personal Care", "Fitness & Health", "Wearable Tech", "Travel & Luggage", "Photography", "Home & Garden", "Gardening & Lawn Care", 
                   "Home Decor", "Kitchen Accessories", "Parenting & Baby Care", "Laptops", "Office Supplies", "Mobile Phones", "Tablets", 
                   "Video Games", "Electronics", "Cycling Accessories"]
category_selected = st.selectbox("Category", category_options)

weight = st.number_input("Weight", min_value=0.0, format="%f")
rating = st.number_input("Rating", min_value=1, max_value=5, format="%d")
num_reviews = st.number_input("Number of Reviews", min_value=0, format="%d")

# Text inputs for numerical features (if needed)
length = st.text_input("Length (optional)", "")  # Update if needed based on your data
width = st.text_input("Width (optional)", "")  # Update if needed based on your data
height = st.text_input("Height (optional)", "")  # Update if needed based on your data

def load_model(model_path):
  """Loads a pickled model from the specified path.

  Args:
      model_path (str): Path to the pickled model file.

  Returns:
      object: The loaded model object.
  """
  try:
    with open(model_path, 'rb') as file:
      model = pickle.load(file)
      return model
  except FileNotFoundError:
    print(f"Error: Model file not found at {model_path}")
    return None

if st.button("Recommend Products"):
  loaded_model = load_model("product_price_recommendation_model.pkl")

  # Encode categorical features (replace with your encoding method)
  color_encoding = {
    "Black": 0,
    "White": 1,
    "Silver": 2,
    "Blue": 3,
    "Green": 4,
    "Red": 5,
    "RGB": 6,
    "Brown": 7,
    "Beige": 8
}  # Define your encoding dictionary
  material_encoding = {
    "Plastic": 0,
    "Metal": 1,
    "Wood": 2,
    "Fabric": 3,
    "Nylon": 4,
    "Aluminum": 5,
    "Glass": 6,
    "Stainless Steel": 7,
    "Leather": 8,
    "Paper": 9,
    "Foam": 10
}  # Define your encoding dictionary
  category_encoding = {
    "Home & Office": 0,
    "Kitchen Appliances": 1,
    "Audio Devices": 2,
    "Computer Accessories": 3,
    "Car Accessories": 4,
    "Outdoor & Sports": 5,
    "Home Security": 6,
    "Home Appliances": 7,
    "Health & Wellness": 8,
    "Apparel & Accessories": 9,
    "Home Automation": 10,
    "Mobile Accessories": 11,
    "Pet Supplies": 12,
    "Personal Care": 13,
    "Fitness & Health": 14,
    "Wearable Tech": 15,
    "Travel & Luggage": 16,
    "Photography": 17,
    "Home & Garden": 18,
    "Gardening & Lawn Care": 19,
    "Home Decor": 20,
    "Kitchen Accessories": 21,
    "Parenting & Baby Care": 22,
    "Laptops": 23,
    "Office Supplies": 24,
    "Mobile Phones": 25,
    "Tablets": 26,
    "Video Games": 27,
    "Electronics": 28,
    "Cycling Accessories": 29
}

  # Prepare input data (consider handling missing values for optional features)
  inputs = [
      float(weight),
      float(rating),
      int(num_reviews),
      category_encoding[category_selected],
      float(length) if length else 0.0,  # Handle missing values if applicable
      float(width) if width else 0.0,  # Handle missing values if applicable
      float(height) if height else 0.0,  # Handle missing values if applicable
      color_encoding[color_selected],
      material_encoding[material_selected]
  ]
  print(loaded_model)
  inputs = np.array(inputs)
  print("inputs: ")
  print(inputs)
  output = loaded_model.predict([inputs])
  print(output)
  formatted_output = f"{output[0]:.2f} rupees"
  st.write(formatted_output, style="color: green; font-weight: bold;")