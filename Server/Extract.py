import pytesseract
from PIL import Image
import sys
import json
import os


dataofimage = sys.argv[1]

# Path to Tesseract executable (modify this according to your installation)
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'


# Function to extract text from an image
def extract_text_from_image(image_path):
    try:
        # Open the image file
        with Image.open(image_path) as img:
            # Use Tesseract OCR to extract text from the image
            extracted_text = pytesseract.image_to_string(img)
            return extracted_text
    except Exception as e:
        print("Error:", e)
        return None

# Path to the image file
image_path = dataofimage

# Extract text from the image
extracted_text = extract_text_from_image(image_path)

# Print the extracted text
if extracted_text:
    print("Extracted text from the image:")
    print(extracted_text)
else:
    print("Failed to extract text from the image.")
