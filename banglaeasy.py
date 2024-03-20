import streamlit as st
from PIL import Image
import easyocr
import io

st.title('Bangla Word Recognition')

# Function to perform OCR on the selected image
def perform_ocr(image):
    reader = easyocr.Reader(['bn'])
    result = reader.readtext(image)
    text = ' '.join([text[1] for text in result])
    return text

uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
use_camera = st.checkbox("Use Camera Input")

if use_camera:
    st.warning("Camera input is not supported with EasyOCR. Please upload an image instead.")

if uploaded_image is not None:
    # Display uploaded image
    image = Image.open(uploaded_image)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Perform OCR on the image
    text = perform_ocr(image)
    st.write('## Recognized Bangla Word:')
    st.write(text)

# Add footer
st.markdown("---")
st.write("Developed by Adnan")
