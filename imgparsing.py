import streamlit as st
import os
from PIL import Image
import fitz  # PyMuPDF for PDF handling
import google.generativeai as genai
import io

# Configure the hardcoded API key
API_KEY = "AIzaSyAr_1w_MtufxQ7XJkL4X-Ve37Jv3yzns8Q"  # Replace with your actual API key

# Function to extract images from PDF
def extract_images_from_pdf(pdf_file):
    images = []
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        for img_index, img in enumerate(page.get_images(full=True)):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            img = Image.open(io.BytesIO(image_bytes))
            images.append(img)
    return images

# Streamlit UI
st.title('PDF Image Captioning')

uploaded_pdf = st.file_uploader("Choose a PDF file...", type=["pdf"])

if uploaded_pdf is not None:
    if st.button('Upload and Process'):
        # Ensure the API key is valid
        if API_KEY.strip() == '':
            st.error('Enter a valid API key in the code')
        else:
            # Extract images from the uploaded PDF
            images = extract_images_from_pdf(uploaded_pdf)

            if images:
                try:
                    # Configure the Google Generative AI model
                    genai.configure(api_key=API_KEY)
                    model = genai.GenerativeModel('gemini-1.5-flash')  # Using gemini-1.5-flash

                    # Loop through each image and generate captions
                    for i, img in enumerate(images):
                        # Generate caption for the image
                        caption_response = model.generate_content(["Write a caption for the image in English", img])
                        caption = caption_response.text

                        # Display the image and the caption in bold
                        st.image(img, caption=f"Image {i+1}")
                        st.markdown(f"**Caption {i+1}: {caption}**")

                except Exception as e:
                    error_msg = str(e)
                    st.error(f"Failed to configure API or process images due to: {error_msg}")
            else:
                st.write("No images found in the PDF.")
