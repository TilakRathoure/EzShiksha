import sys
from PIL import Image
import pytesseract
import os
import shutil

# ------------------ Detect Tesseract dynamically ------------------ #
tesseract_path = shutil.which("tesseract")
if tesseract_path:
    pytesseract.pytesseract.tesseract_cmd = tesseract_path
else:
    raise EnvironmentError(
        "Tesseract OCR is not installed or not in PATH. "
        "Please install it. "
        "Linux: sudo apt install tesseract-ocr\n"
        "MacOS: brew install tesseract\n"
        "Windows: Download from https://github.com/UB-Mannheim/tesseract/wiki"
    )

# ------------------ Function to extract text ------------------ #
def extract_text_from_image(image_path: str) -> str:
    """
    Extracts text from an image using Tesseract OCR.
    Works with printed text in most languages.
    """
    try:
        # Open image using Pillow
        image = Image.open(image_path)

        # Run OCR
        extracted_text = pytesseract.image_to_string(image)

        # Clean up text (remove empty lines, extra spaces)
        cleaned_text = " ".join(extracted_text.split())

        return cleaned_text if cleaned_text else None
    except Exception as e:
        print("Error while extracting text:", e)
        return None

# ------------------ Main ------------------ #
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python extract.py <image_path>")
        sys.exit(1)

    image_path = sys.argv[1]

    # Ensure the file exists before processing
    if not os.path.isfile(image_path):
        print(f"Error: Image file does not exist: {image_path}")
        sys.exit(1)

    text = extract_text_from_image(image_path)

    if text:
        print(text)
    else:
        print("❌ Failed to extract text from the image.")
