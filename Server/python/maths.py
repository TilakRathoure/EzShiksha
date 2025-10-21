import re
import sys
from sympy import symbols, Eq, solve, log, sin, pi, sqrt
from PIL import Image
import pytesseract
import shutil
import os

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

# ------------------ OCR Using Tesseract ------------------ #
def extract_text_from_image(image_path: str) -> str:
    try:
        image = Image.open(image_path)
        extracted_text = pytesseract.image_to_string(image)
        cleaned_text = " ".join(extracted_text.split())
        return cleaned_text.replace('A', '^')  # optional fix
    except Exception as e:
        print("Error while extracting text:", e)
        return None

# ------------------ Equation Classification ------------------ #
def classify_equation(equation: str) -> str:
    equation = equation.strip()
    
    if re.match(r'^\s*([-+]?\d+\.?\d*)\s*\*\s*x\s*([-+])\s*([-+]?\d+\.?\d*)\s*=\s*0\s*$', equation):
        return "Linear Equation"
    if re.match(r'^\s*([-+]?\d+\.?\d*)\s*\*\s*x\^2\s*([-+])\s*([-+]?\d+\.?\d*)\s*\*\s*x\s*([-+])\s*([-+]?\d+\.?\d*)\s*=\s*0\s*$', equation):
        return "Quadratic Equation"
    if re.match(r'^\s*([-+]?\d+\.?\d*)\s*\*\s*x\^3\s*([-+])\s*([-+]?\d+\.?\d*)\s*\*\s*x\^2\s*([-+])\s*([-+]?\d+\.?\d*)\s*\*\s*x\s*([-+])\s*([-+]?\d+\.?\d*)\s*=\s*0\s*$', equation):
        return "Cubic Equation"
    if re.match(r'^\s*([-+]?\d+\.?\d*)\s*\*\s*x\^4\s*([-+])\s*([-+]?\d+\.?\d*)\s*\*\s*x\^3\s*([-+])\s*([-+]?\d+\.?\d*)\s*\*\s*x\^2\s*([-+])\s*([-+]?\d+\.?\d*)\s*\*\s*x\s*([-+])\s*([-+]?\d+\.?\d*)\s*=\s*0\s*$', equation):
        return "Quartic Equation"
    if re.match(r'^\s*([-+]?\d+\.?\d*)\s*\*\*?\s*x\s*=\s*([-+]?\d+\.?\d*)\s*$', equation):
        return "Exponential Equation"
    if re.match(r'^\s*([-+]?\d+\.?\d*)\s*\/\s*x\s*([-+])\s*([-+]?\d+\.?\d*)\s*=\s*([-+]?\d+\.?\d*)\s*$', equation):
        return "Rational Equation"
    if re.match(r'^\s*log\s*\(\s*x\s*\)\s*=\s*([-+]?\d+\.?\d*)\s*$', equation):
        return "Logarithmic Equation"
    if re.match(r'^\s*(sin|cos|tan)\s*\(\s*x\s*\)\s*=\s*([-+]?\d+\.?\d*)\s*$', equation):
        return "Trigonometric Equation"
    if re.match(r'^\s*sqrt\s*\(\s*x\s*\)\s*=\s*([-+]?\d+\.?\d*)\s*$', equation):
        return "Radical Equation"
    if re.match(r'^\s*([-+]?\d+\.?\d*)\s*\*\s*x\^2\s*\+\s*([-+]?\d+\.?\d*)\s*\*\s*y\^2\s*=\s*([-+]?\d+\.?\d*)\s*$', equation):
        return "Ellipse (Conic Section Equation)"
    if re.match(r'^\s*x\^2\s*\/\s*([-+]?\d+\.?\d*)\s*\-\s*y\^2\s*\/\s*([-+]?\d+\.?\d*)\s*=\s*([-+]?\d+\.?\d*)\s*$', equation):
        return "Hyperbola (Conic Section Equation)"
    if re.match(r'^\s*\|\s*([-+]?\d+\.?\d*)\s*\*\s*x\s*([-+])\s*([-+]?\d+\.?\d*)\s*\|\s*=\s*([-+]?\d+\.?\d*)\s*$', equation):
        return "Absolute Value Equation"
    
    return "Other"

# ------------------ Equation Solvers ------------------ #
def solve_linearQuadraticCubicQuarticRational_equation(equation_str):
    equation_str = equation_str.replace('^', '**')
    left_side, right_side = equation_str.split('=')
    x = symbols('x')
    equation = Eq(eval(left_side), eval(right_side))
    return solve(equation, x)

def solve_exponential_equation(equation_str):
    equation_str = equation_str.replace('^', '**')
    left, right = equation_str.split('=')
    base = int(left.split('**')[0])
    x = symbols('x')
    equation = Eq(base**x, int(right))
    return solve(equation, x)

def solve_logarithmic_equation(equation_str):
    _, result = equation_str.split('=')
    x = symbols('x')
    equation = Eq(log(x, 10), int(result))
    return solve(equation, x)

def solve_trigonometric_equation(equation_str):
    _, result = equation_str.split('=')
    x = symbols('x')
    equation = Eq(sin(x), float(result))
    solutions = solve(equation, x)
    return [s * 180 / pi.evalf() for s in solutions]

def solve_radical_equation(equation_str):
    _, result = equation_str.split('=')
    x = symbols('x')
    equation = Eq(sqrt(x), float(result))
    return solve(equation, x)

def solve_ellipseHyperbola_equation(equation_str):
    left, right = equation_str.split('=')
    x, y = symbols('x y')
    equation = Eq(eval(left), eval(right))
    return solve(equation)

def solve_equation(classification, equation_str):
    if classification in ["Linear Equation", "Quadratic Equation", "Cubic Equation", "Quartic Equation", "Rational Equation"]:
        return solve_linearQuadraticCubicQuarticRational_equation(equation_str)
    elif classification == "Exponential Equation":
        return solve_exponential_equation(equation_str)
    elif classification == "Logarithmic Equation":
        return solve_logarithmic_equation(equation_str)
    elif classification == "Trigonometric Equation":
        return solve_trigonometric_equation(equation_str)
    elif classification == "Radical Equation":
        return solve_radical_equation(equation_str)
    elif classification in ["Ellipse (Conic Section Equation)", "Hyperbola (Conic Section Equation)"]:
        return solve_ellipseHyperbola_equation(equation_str)
    else:
        return "Sorry, the solution of this equation cannot be found."

# ------------------ Main ------------------ #
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <image_path>")
        sys.exit(1)

    image_path = sys.argv[1]

    if not os.path.isfile(image_path):
        print(f"Error: Image file does not exist: {image_path}")
        sys.exit(1)

    extracted_text = extract_text_from_image(image_path)

    if not extracted_text:
        print("❌ Failed to extract text from the image.")
        sys.exit(1)

    classification = classify_equation(extracted_text)
    solutions = solve_equation(classification, extracted_text)

    print(f"Equation: {extracted_text}")
    print(f"Classification: {classification}")
    print(f"Solution: {solutions}\n")
