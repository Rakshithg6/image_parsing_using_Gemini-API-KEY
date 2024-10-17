# Image Parsing from PDF using Google Gemini API

This project is a Streamlit-based application that extracts images from PDF files and generates captions for them using Google's Gemini AI model.

## Features

- Extract images from a PDF file.
- Generate captions for the extracted images using Google's Gemini AI.
- Display both the images and their captions in a user-friendly web interface.

## Installation

1. **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Create and activate a virtual environment**:
    - On Windows:
      ```bash
      python -m venv venv
      .\venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      python3 -m venv venv
      source venv/bin/activate
      ```

3. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set your Google Gemini API Key**:
    - Open the `app.py` file and replace `API_KEY` with your actual Google Gemini API key:
      ```python
      API_KEY = "YOUR_API_KEY"
      ```

5. **Run the app**:
    ```bash
    streamlit run app.py
    ```

6. **Open the app in your browser**:
    - The app will be available at `http://localhost:8501`.

## Usage

1. Upload a PDF file containing images.
2. The app will extract the images from the PDF.
3. For each extracted image, the app will generate and display a caption using the Gemini AI model.

## Requirements

- Python 3.x
- Libraries used:
  - `streamlit`
  - `Pillow`
  - `PyMuPDF (fitz)`
  - `google-generativeai`
