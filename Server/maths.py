import re
from sympy import symbols, Eq, solve, log, sin, pi, sqrt
import sys
import easyocr  # OCR alternative to pytesseract

# ------------------ Initialize EasyOCR Reader ------------------ #
# Disable progress output
reader = easyocr.Reader(['en'], gpu=False, verbose=False)

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
    # Convert radians to degrees
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

# ------------------ OCR Using EasyOCR ------------------ #
def extract_text_from_image(image_path: str) -> str:
    results = reader.readtext(image_path)
    extracted_text = " ".join([res[1] for res in results])
    return extracted_text.replace('A', '^')  # fix misread '^'

# ------------------ Main ------------------ #
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <image_path>")
        sys.exit(1)

    image_path = sys.argv[1]
    extracted_text = extract_text_from_image(image_path)

    classification = classify_equation(extracted_text)
    solutions = solve_equation(classification, extracted_text)

    print(f"Equation: {extracted_text}")
    print(f"Classification: {classification}")
    print(f"Solution: {solutions}\n")
