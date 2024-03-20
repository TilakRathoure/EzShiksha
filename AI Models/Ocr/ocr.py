!pip install pytesseract
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageEnhance
import pytesseract
import re

class OCRApp:
    def init(self, master):
        self.master = master
        self.master.title("OCR Application")

        self.image_label = tk.Label(self.master, text="No image loaded")
        self.image_label.pack()

        self.load_button = tk.Button(self.master, text="Load Image", command=self.load_image)
        self.load_button.pack()

        self.perform_ocr_button = tk.Button(self.master, text="Perform OCR", command=self.perform_ocr)
        self.perform_ocr_button.pack()

        self.ocr_text = tk.Text(self.master, wrap=tk.WORD, height=10, width=50)
        self.ocr_text.pack()

        self.image_path = None
        self.image = None

    def load_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", ".jpg;.jpeg;*.png")])
        if file_path:
            self.image_path = file_path
            self.image = Image.open(self.image_path)
            self.display_image()

    def display_image(self):
        if self.image:
            self.image.thumbnail((400, 400))  # Resize image for display
            photo = ImageTk.PhotoImage(self.image)
            self.image_label.config(image=photo)
            self.image_label.image = photo
            self.perform_ocr_button.config(state="normal")
            self.ocr_text.delete(1.0, tk.END)
        else:
            self.image_label.config(text="No image loaded")
            self.perform_ocr_button.config(state="disabled")

    def perform_ocr(self):
        if self.image:
            # Preprocess the image to enhance text clarity
            enhanced_image = self.enhance_image_contrast(self.image)

            # Perform OCR on the enhanced image
            text = pytesseract.image_to_string(enhanced_image)

            # Process OCR results for better handling of numbers and equations
            processed_text = self.process_ocr_text(text)

            self.ocr_text.insert(tk.END, processed_text)
        else:
            self.ocr_text.insert(tk.END, "No image loaded for OCR")

    def enhance_image_contrast(self, image):
        enhancer = ImageEnhance.Contrast(image)
        enhanced_image = enhancer.enhance(2.0)  # Enhance contrast by a factor of 2
        return enhanced_image

    def process_ocr_text(self, text):
        # Process OCR results to improve handling of numbers and equations
        # Here, you can add custom logic based on your specific requirements
        # For example, you can use regular expressions to identify and format numbers or equations
        
        # Example: Format numbers detected in the text
        text = re.sub(r'(\d+)', r'<b>\1</b>', text)  # Wrap numbers with <b> tags for highlighting
        
        # Example: Identify and format simple equations (e.g., addition, subtraction)
        equations = re.findall(r'(\d+)\s*[\+\-\/]\s(\d+)', text)
        for equation in equations:
            result = self.evaluate_simple_equation(*equation)
            text = text.replace(''.join(equation), f'{equation[0]} + {equation[1]} = {result}')

        return text

    def evaluate_simple_equation(self, operand1, operand2, operator):
        operand1 = int(operand1)
        operand2 = int(operand2)
        if operator == '+':
            return operand1 + operand2
        elif operator == '-':
            return operand1 - operand2
        elif operator == '*':
            return operand1 * operand2
        elif operator == '/':
            if operand2 != 0:
                return operand1 / operand2
            else:
                return "Division by zero"

def main():
    root = tk.Tk()
    app = OCRApp(root)
    root.mainloop()

if __name__ == "main":
    main()


from google.colab import drive
from PIL import Image
import pytesseract

# Mount Google Drive
drive.mount('/content/drive')

# Path to the uploaded image file in Google Drive
image_path = "/content/drive/MyDrive/Sample.png"

# Load the image
image = Image.open(image_path)

# Perform OCR
text = pytesseract.image_to_string(image)

# Display OCR results
print(text)