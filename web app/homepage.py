import streamlit as st
import threading

# st.set_page_config(layout="wide")

# video_html = """
# <style>
#   #myVideo {
#     position: fixed;
#     top: 0;
#     left: 0;
#     width: 100vw;
#     height: 100vh;
#     object-fit: cover;  /* Ensures video fills the viewport */
#   }

#   .content {
#     position: absolute;  /* Avoid overlapping video with content */
#     bottom: 0;
#     background: rgba(0, 0, 0, 0.5);
#     color: #f1f1f1;
#     width: 100%;
#     padding: 20px;
#   }
# </style>
# <video autoplay muted loop id="myVideo">
# 		  <source src="https://videos.pexels.com/video-files/18069166/18069166-uhd_3840_2160_24fps.mp4")>
# 		  Your browser does not support HTML5 video.
# </video>
#         """

# st.markdown(video_html, unsafe_allow_html=True)

st.header( "End to End Machine Learning System for Eccomerce Platforms")
st.subheader("Here are our available systems:")

recommendation_engine = "Product Recommendation Engine"
customer_retention = "Customer Retention"
dynamic_product_price_adjustment = "Dynamically Adjust Product Pricing"
sales_estimation = "Generalized Sales Estimaton"


button_style_recommendation_engine = """
  <style>
    div[data-testid="stButton"] button[data-baseweb="button"] {{
      background-image: url('https://miro.medium.com/v2/resize:fit:1400/0*3SbT1PhHmFdI3Vlo.jpg');
      background-size: cover;
      background-position: center;
      padding: 0px; /* Remove default padding */
      width: 150px;  /* Set button width */
      height: 50px;  /* Set button height */
      border: none;
      cursor: pointer;
    }}
  </style>
  """

page_bg_img = '''
<style>
body {
background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366");
background-size: cover;
}
</style>
'''

def recommendation_engine():
    st.write("")
    # Return a string containing CSS for the recommendation engine button style

def button_style_customer_retention():
    # Return a string containing CSS for the customer retention button style
    pass

def button_style_dynamic_product_price_adjustment():
    # Return a string containing CSS for the dynamic product price adjustment button style
    pass

def button_style_sales_estimation():
    # Return a string containing CSS for the sales estimation button style
    pass


# Button text and functionality
recommendation_engine_text = "Recommendation Engine"
customer_retention_text = "Customer Retention"
dynamic_product_price_adjustment_text = "Dynamic Product Price Adjustment"
sales_estimation_text = "Sales Estimation"

def run_process_in_thread(process_func):
    thread = threading.Thread(target=process_func)
    thread.start()
    st.info(f"Running {process_func.__name__} in the background...")

# Divide buttons into columns
col1, col2 = st.columns(2)

# Create buttons with styled CSS (replace with your generated button styles)
with col1:
    if st.button(recommendation_engine_text):

    
    if st.button(customer_retention_text):
        st.write("Button Clicked!")

with col2:
    if st.button(dynamic_product_price_adjustment_text):
        st.write("Button Clicked!")

    if st.button(sales_estimation_text):
        st.write("Button Clicked!")