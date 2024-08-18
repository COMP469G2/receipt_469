import json

import pytesseract
import requests
import streamlit as st
from PIL import Image

st.title("Image Uploader and Text Extractor")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

    extracted_text = pytesseract.image_to_string(image)

    st.write("Extracted Text:")
    st.write(extracted_text)

    # Model api URL (You have to update this part)
    api_url = "https://www.google.com"

    payload = {"text": extracted_text}

    response = requests.post(api_url, json=payload)

    if response.status_code == 200:
        transformed_output = response.json()

        st.write("Transformed Output:")
        st.json(transformed_output)

        # This part will be the nice formatting part using the json (transformed_output)
    else:
        st.write(
            "Error: Could not get a response from the model. Please try again later."
        )
else:
    st.write("Please upload an image file.")
