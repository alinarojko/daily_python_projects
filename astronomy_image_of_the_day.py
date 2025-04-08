import requests
import streamlit as st

# Prepare API key and API url
api_key = "1eNhR3Bxv71ixJMHVRwb7CVJuLbgq3NIXRZPFR7a"
url = "https://api.nasa.gov/planetary/apod?" \
       f"api_key={api_key}"

# Get the request data as dictionary
responce1 = requests.get(url)
data = responce1.json()

# Extract the image title, url and explanation
title = data["title"]
image_url = data["url"]
explanation = data["explanation"]

# Download the image
image_filepath = "image.png"
responce2 = requests.get(image_url)
with open(image_filepath, "wb") as file:
    file.write(responce2.content)

st.set_page_config(layout="wide")
st.title(title)
st.image(image_filepath)
st.text(explanation)