import sys
import easyocr  # OCR alternative to pytesseract

# Initialize EasyOCR reader without progress bar
reader = easyocr.Reader(['en'], gpu=False, verbose=False)

# ------------------ Function to extract text ------------------ #
def extract_text_from_image(image_path: str) -> str:
    try:
        results = reader.readtext(image_path)
        # Combine all detected text segments
        extracted_text = " ".join([res[1] for res in results])
        return extracted_text
    except Exception as e:
        print("Error:", e)
        return None

# ------------------ Main ------------------ #
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <image_path>")
        sys.exit(1)

    image_path = sys.argv[1]
    extracted_text = extract_text_from_image(image_path)

    if extracted_text:
        print("Extracted text from the image:")
        print(extracted_text)
    else:
        print("Failed to extract text from the image.")
