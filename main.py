import pytesseract
import streamlit as st
from PIL import Image

st.title("Image Uploader and Text Extractor")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)

    st.image(image, caption="Uploaded Image.", use_column_width=True)

    extracted_text = pytesseract.image_to_string(image)

    st.subheader("Extracted Text")
    st.write(extracted_text)

else:
    st.write("Please upload an image file.")
