import streamlit as st
from PIL import Image
import pytesseract
#import functions.functions as fc

class OCR:

    def __init__(self):
        st.set_page_config(page_title="Bangla Word Recognition")
        self.text = ""
        self.analyze_text = False

    def initial(self):
        st.title("Bangla Word Recognition")
        st.write("Optical Character Recognition (OCR) implemented with Python")
        uploaded_image = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

        if uploaded_image:
            image = Image.open(uploaded_image)
            st.image(image, caption='Uploaded Image', use_column_width=True)
            self.text = self.extract_text(image)
            st.write('## Recognized Text:')
            st.write(self.text)
            
           # self.analyze_text = st.checkbox("Analyze Text")
           # if self.analyze_text:
           #     self.show_analysis()

    def extract_text(self, image):
        text = pytesseract.image_to_string(image, lang="ben")
        return text
    
    def show_analysis(self):
        # Your analysis code here
        pass

ocr = OCR()
ocr.initial()
