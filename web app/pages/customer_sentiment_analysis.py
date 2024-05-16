import streamlit as st
from transformers import AutoModelForSequenceClassification
from transformers import AutoTokenizer, AutoConfig
import numpy as np
from scipy.special import softmax
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px  # Import plotly express for interactive charts


def preprocess(text):
    new_text = []
    for t in text.split(" "):
        t = '@user' if t.startswith('@') and len(t) > 1 else t
        t = 'http' if t.startswith('http') else t
        new_text.append(t)
    return " ".join(new_text)

model_path = "daveni/twitter-xlm-roberta-emotion-es"
tokenizer = AutoTokenizer.from_pretrained(model_path)
config = AutoConfig.from_pretrained(model_path)
model = AutoModelForSequenceClassification.from_pretrained(model_path)

# Stunning Background Image
page_bg_img = '''
<style>
body {
  background-image: url("https://images.unsplash.com/photo-1584283520432-39545c39e43a?fit=crop&w=1920&h=1080");
  background-size: cover;
  background-attachment: fixed;
  font-family: sans-serif;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

# Informative Title
st.title("Unlocking the Language of Emotions")
st.write("This web app utilizes the power of DistilBERT, a fine-tuned language model, to unveil the emotional undercurrents within your text. It can discern amongst seven core emotions: joy, sadness, surprise, anger, fear, disgust, and 'others'.")

# Interactive Text Input with Stylish Design
text = st.text_input("Enter the customer message...", key="user_text")
text = preprocess(text)
print(text)
encoded_input = tokenizer(text, return_tensors='pt')
output = model(**encoded_input)

# Get predicted scores and labels
scores = output[0][0].detach().numpy()
scores = softmax(scores)

# Print labels and scores (modify to display in Streamlit)
ranking = np.argsort(scores)
ranking = ranking[::-1]

st.write("**Estimate Emotion:**")

print(ranking)

map = {}

for i in range(scores.shape[0]):
    l = config.id2label[ranking[i]]
    s = scores[ranking[i]]

    map[l] = s 
    print(f"{i+1}) {l} {np.round(float(s), 4)}")

print(type(ranking))

# Button with Improved Design
convert_button = st.button("Get the sentiment")

# Output with Dynamic Text Color
if convert_button:
    # Use the created map for emotion labels
    emotion_labels = list(map.keys())  # Extract labels from the map
    emotion_scores = list(map.values())  # Extract scores from the map

    # Create a dictionary to store labels and scores
    emotion_data = {"emotions": emotion_labels, "scores": emotion_scores}

    # Create a pie chart using plotly express
    fig = px.pie(emotion_data, values='scores', names='emotions', title='Customer Sentiment Distribution')

    # Customize the chart appearance (optional)
    fig.update_layout(
        title_x=0.5,  # Center the title
        font_size=14,  # Adjust font size for readability
    )

    # Display the pie chart on Streamlit
    st.plotly_chart(fig)