import json

import pytesseract
import streamlit as st
from PIL import Image

st.title("Image Uploader and Text Extractor")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

    extracted_text = pytesseract.image_to_string(image)

    # Pretend that we send the extracted_text to the model api and received the test_json_data from it.

    test_json_data = {
        "summary": "This document discusses the impact of climate change on polar bear populations.",
        "entities": [
            {"type": "Animal", "name": "polar bear", "confidence": 0.98},
            {"type": "Location", "name": "Arctic", "confidence": 0.95},
        ],
        "sentiment": {"polarity": "negative", "confidence": 0.85},
        "key_points": [
            "Rising temperatures reduce the sea ice habitat of polar bears.",
            "Food scarcity leads to decreased polar bear populations.",
        ],
    }

    st.write("Transformed Output:")
    st.json(test_json_data)
    print(test_json_data)

else:
    st.write("Please upload an image file.")
