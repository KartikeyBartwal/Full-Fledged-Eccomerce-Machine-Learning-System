import streamlit as st

# Stunning Background Image
page_bg_img = '''
<style>
body {
  background-image: url("https://images.unsplash.com/photo-1600088921122-fca1781f7cbf?fit=crop&w=1920&h=1080");  background-size: cover;
  background-attachment: fixed;  font-family: sans-serif;  }
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

# Stylish Button Design
button_style = '''
<style>
div[data-testid="stButton"] button[data-baseweb="button"] {
  background-color: #F08080;  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
  border-radius: 5px;
  box-shadow: 0px 5px 10px rgba(0, 0, 0, 0.2);  }

div[data-testid="stButton"] button[data-baseweb="button"]:hover {
  background-color: #D7191C;  }
</style>
'''
st.markdown(button_style, unsafe_allow_html=True)

# Informative Title and Text
st.title("Product Recommendation Score")

# User Input with Clear Labels and Explanations
num_clicks_similar_products = st.slider(
    "Clicks on Similar Products",
    min_value=0,
    max_value=100,
    key="num_clicks_similar",
    help="How many times did you click on similar products while browsing?"
)
num_similar_purchased = st.number_input(
    "Similar Products Purchased",
    min_value=0,
    key="num_similar_purchased",
    help="How many similar products have you bought in the past?"
)

gender_options = ["Male", "Female", "Non-binary"]
gender = st.radio("Gender", options=gender_options, key="gender")

median_price = st.number_input(
    "Median Purchase Price (₹)",
    min_value=0.0,
    format="%f",
    key="median_price",
    help="What's the average price range you usually consider?"
)

rating_labels = ["Very Poor", "Poor", "Average", "Good", "Excellent"]
product_rating = st.selectbox(
    "Your Rating of the Product", options=rating_labels, key="product_rating", help="How would you rate this product?"
)

avg_rating_similar_index = st.slider(
    "Average Rating of Similar Products",
    min_value=0,
    max_value=len(rating_labels) - 1,
    key="avg_rating_similar",
    help="What's the general rating you've seen for similar products?"
)

product_brand = st.text_input("Brand of the Product (Optional)", key="product_brand", help="If you know the brand, enter it here.")

# Call to Action Button with Improved Design
submit_button = st.button("Recommendation Score")

# Display Recommendations (Replace with your recommendation logic)
if submit_button:
    st.write("**Based on your input, here are some product recommendations for you:**")
    # Insert your recommendation logic here, potentially using
