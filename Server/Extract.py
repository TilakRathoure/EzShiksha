import sys
from PIL import Image
import pytesseract

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

        # Clean up text (remove empty lines, etc.)
        cleaned_text = " ".join(extracted_text.split())

        return cleaned_text if cleaned_text else None
    except Exception as e:
        print("Error while extracting text:", e)
        return None

# ------------------ Main ------------------ #
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python ocr_extractor.py <image_path>")
        sys.exit(1)

    image_path = sys.argv[1]
    text = extract_text_from_image(image_path)

    if text:
        print("\n🟩 Extracted text from the image:\n")
        print(text)
    else:
        print("\n❌ Failed to extract text from the image.")
