import re
from sympy import symbols, Eq, solve, simplify, log, sin, pi, sqrt
import sys
import json


def classify_equation(equation):
    # Check for linear equation (ax + b = 0)
    if re.match(r'^\s*([-+]?\d+\.?\d*)\s*\*\s*x\s*([-+])\s*([-+]?\d+\.?\d*)\s*=\s*0\s*$', equation):
        return "Linear Equation"

    # Check for quadratic equation (ax^2 + bx + c = 0)
    if re.match(r'^\s*([-+]?\d+\.?\d*)\s*\*\s*x\^2\s*([-+])\s*([-+]?\d+\.?\d*)\s*\*\s*x\s*([-+])\s*([-+]?\d+\.?\d*)\s*=\s*0\s*$', equation):
        return "Quadratic Equation"

    # Check for cubic equation (ax^3 + bx^2 + cx + d = 0)
    if re.match(r'^\s*([-+]?\d+\.?\d*)\s*\*\s*x\^3\s*([-+])\s*([-+]?\d+\.?\d*)\s*\*\s*x\^2\s*([-+])\s*([-+]?\d+\.?\d*)\s*\*\s*x\s*([-+])\s*([-+]?\d+\.?\d*)\s*=\s*0\s*$', equation):
        return "Cubic Equation"

    # Check for quartic equation (ax^4 + bx^3 + cx^2 + dx + e = 0)
    if re.match(r'^\s*([-+]?\d+\.?\d*)\s*\*\s*x\^4\s*([-+])\s*([-+]?\d+\.?\d*)\s*\*\s*x\^3\s*([-+])\s*([-+]?\d+\.?\d*)\s*\*\s*x\^2\s*([-+])\s*([-+]?\d+\.?\d*)\s*\*\s*x\s*([-+])\s*([-+]?\d+\.?\d*)\s*=\s*0\s*$', equation):
        return "Quartic Equation"

    # Check for exponential equation (a^x = c)
    if re.match(r'^\s*([-+]?\d+\.?\d*)\s*\*\*?\s*x\s*=\s*([-+]?\d+\.?\d*)\s*$', equation):
        return "Exponential Equation"

    # Check for rational equation (a/x + b = c)
    if re.match(r'^\s*([-+]?\d+\.?\d*)\s*\/\s*x\s*([-+])\s*([-+]?\d+\.?\d*)\s*=\s*([-+]?\d+\.?\d*)\s*$', equation):
        return "Rational Equation"

    # Check for logarithmic equation (log(x) = c)
    if re.match(r'^\s*log\s*\(\s*x\s*\)\s*=\s*([-+]?\d+\.?\d*)\s*$', equation):
        return "Logarithmic Equation"

    # Check for trigonometric equation (sin(x) = c, cos(x) = c, tan(x) = c)
    if re.match(r'^\s*(sin|cos|tan)\s*\(\s*x\s*\)\s*=\s*([-+]?\d+\.?\d*)\s*$', equation):
        return "Trigonometric Equation"

    # Check for radical equation (sqrt(x) = c)
    if re.match(r'^\s*sqrt\s*\(\s*x\s*\)\s*=\s*([-+]?\d+\.?\d*)\s*$', equation):
        return "Radical Equation"

    # Check for conic section equations
    if re.match(r'^\s*([-+]?\d+\.?\d*)\s*\*\s*x\^2\s*\+\s*([-+]?\d+\.?\d*)\s*\*\s*y\^2\s*=\s*([-+]?\d+\.?\d*)\s*$', equation):
        return "Ellipse (Conic Section Equation)"
    if re.match(r'^\s*x\^2\s*\/\s*([-+]?\d+\.?\d*)\s*\-\s*y\^2\s*\/\s*([-+]?\d+\.?\d*)\s*=\s*([-+]?\d+\.?\d*)\s*$', equation):
        return "Hyperbola (Conic Section Equation)"

    # Check for absolute value equations
    if re.match(r'^\s*\|\s*([-+]?\d+\.?\d*)\s*\*\s*x\s*([-+])\s*([-+]?\d+\.?\d*)\s*\|\s*=\s*([-+]?\d+\.?\d*)\s*$', equation):
        return "Absolute Value Equation"

    # If none of the above, classify as other
    return "Other"

def solve_linearQuadraticCubicQuarticRational_equation(equation_str):
    # Replace '^' with '**'
    equation_str = equation_str.replace('^', '**')
    # Parse the equation
    equation_parts = equation_str.split('=')
    left_side = equation_parts[0].strip()
    right_side = equation_parts[1].strip()

    # Define the variable
    x = symbols('x')

    equation = Eq(eval(left_side), eval(right_side))

    # Solve the equation for x
    solutions = solve(equation, x)

    return solutions


def solve_exponential_equation(equation_str):
    # Replace '^' with '**'
    equation_str = equation_str.replace('^', '**')
    # Parse the equation
    equation_parts = equation_str.split('=')
    base_and_exponent = equation_parts[0].strip().split('**')
    base = int(base_and_exponent[0].strip())
    result = int(equation_parts[1].strip())

    # Define the variable
    x = symbols('x')

    # Define the equation
    equation = Eq(base**x, result)

    # Solve the equation for x
    solutions = solve(equation, x)

    return solutions


def solve_logarithmic_equation(equation_str):
    # Replace '^' with '**'
    equation_str = equation_str.replace('^', '**')
    # Parse the equation
    equation_parts = equation_str.split('=')
    base = 10  # Base 10 logarithm
    result = int(equation_parts[1].strip())

    # Define the variable
    x = symbols('x')

    # Define the equation
    equation = Eq(log(x, base), result)

    # Solve the equation for x
    solutions = solve(equation, x)

    return solutions


def solve_trigonometric_equation(equation_str):
    # Replace '^' with '**'
    equation_str = equation_str.replace('^', '**')
    # Parse the equation
    equation_parts = equation_str.split('=')
    result = float(equation_parts[1].strip())

    # Define the variable
    x = symbols('x')

    # Define the equation
    equation = Eq(sin(x), result)

    # Solve the equation for x
    solutions = solve(equation, x)

    # Convert solutions from radians to degrees
    solutions_degrees = [s * 180 / pi.evalf() for s in solutions]

    return solutions_degrees


def solve_radical_equation(equation_str):
    # Replace '^' with '**'
    equation_str = equation_str.replace('^', '**')
    # Parse the equation
    equation_parts = equation_str.split('=')
    result = float(equation_parts[1].strip())

    # Define the variable
    x = symbols('x')

    # Define the equation
    equation = Eq(sqrt(x), result)

    # Solve the equation for x
    solutions = solve(equation, x)

    return solutions


def solve_ellipseHyperbola_equation(equation_str):
    # Replace '^' with '**'
    equation_str = equation_str.replace('^', '**')
    # Parse the equation
    equation_parts = equation_str.split('=')
    left_side = equation_parts[0].strip()
    right_side = equation_parts[1].strip()

    # Define the variables
    x, y = symbols('x y')

    # Define the equation
    equation = Eq(eval(left_side), eval(right_side))

    # Solve the equation
    solutions = solve(equation)

    return solutions

def solve_equation(classification, equation_str):
    if classification in ["Linear Equation","Quadratic Equation","Cubic Equation","Quartic Equation","Rational Equation"]:
        return solve_linearQuadraticCubicQuarticRational_equation(equation_str)
    elif classification == "Exponential Equation":
        return solve_exponential_equation(equation_str)
    elif classification == "Logarithmic Equation":
        return solve_logarithmic_equation(equation_str)
    elif classification == "Trigonometric Equation":
        return solve_trigonometric_equation(equation_str)
    elif classification == "Radical Equation":
        return solve_radical_equation(equation_str)
    elif classification in ["Ellipse (Conic Section Equation)","Hyperbola (Conic Section Equation)"]:
        return solve_ellipseHyperbola_equation(equation_str)
    else:
        return "Sorry, the solution of this equation cannot be found."
    
import cv2
from PIL import Image
import pytesseract
# Function to extract text from an image
def extract_text_from_image(image_path):
    # Read the image
    image = cv2.imread(image_path)
    
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Use Tesseract OCR to extract text from the image
    extracted_text = pytesseract.image_to_string(gray_image)
    
    return extracted_text

# Example image path

dataofimage = sys.argv[1]

image_path = dataofimage

# Extract text from the image

extracted_text = extract_text_from_image(image_path)

extracted_text=extracted_text.replace('A', '^')

    # "3*x^3 - 16*x^2 + 23*x - 6 = 0",  # Cubic Equation

    # "2**x = 8"
    # "log(x) = 2"


    # "3*x^2 + 4*y^2 = 12" 

# Classify and print the equations
classification = classify_equation(extracted_text)
solutions = solve_equation(classification,extracted_text)
print(f"Equation: {extracted_text}")
print(f"Classification: {classification}")
print(f"Solution: {solutions}\n")

"""

---

"""