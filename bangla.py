import streamlit as st
from PIL import Image
import pytesseract
import io
import numpy as np

st.title('Bangla word recognition')

# Function to perform OCR on the selected image
def perform_ocr(image):
    text = pytesseract.image_to_string(image, lang='por')
    return text

uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
use_camera = st.checkbox("Use Camera Input")

if use_camera:
    camera_image = st.camera_input("Take a picture")
    if camera_image is not None:
        # Convert camera image to bytes
        image_bytes = camera_image.getvalue()

        # Load bytes data into PIL Image
        image = Image.open(io.BytesIO(image_bytes))

        # Perform OCR on the camera image
        st.image(image, caption='Camera Image', use_column_width=True)
        text = perform_ocr(image)
        st.write('## Recognized Bangla word:')
        st.write(text)
elif uploaded_image is not None:
    # Display uploaded image
    image = Image.open(uploaded_image)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Perform OCR on the image
    text = perform_ocr(image)
    st.write('## Recognized Bangla word:')
    st.write(text)
# Add footer
st.markdown("---")
st.write("Developed by Adnan")
