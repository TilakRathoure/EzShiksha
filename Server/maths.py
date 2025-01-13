import re
from sympy import symbols, Eq, solve, simplify, log, sin, pi, sqrt
import sys
import json
import cv2
from PIL import Image
import pytesseract

def classify_equation(equation):
    try:
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
    except Exception as e:
        print(f"Error in classify_equation function: {e}")
        return "Error"

def solve_linearQuadraticCubicQuarticRational_equation(equation_str):
    try:
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
    except Exception as e:
        print(f"Error solving linear/quadratic/cubic/quartic/rational equation: {e}")
        return []

def solve_exponential_equation(equation_str):
    try:
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
    except Exception as e:
        print(f"Error solving exponential equation: {e}")
        return []

def solve_logarithmic_equation(equation_str):
    try:
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
    except Exception as e:
        print(f"Error solving logarithmic equation: {e}")
        return []

def solve_trigonometric_equation(equation_str):
    try:
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
    except Exception as e:
        print(f"Error solving trigonometric equation: {e}")
        return []

def solve_radical_equation(equation_str):
    try:
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
    except Exception as e:
        print(f"Error solving radical equation: {e}")
        return []

def solve_ellipseHyperbola_equation(equation_str):
    try:
        # Replace '^' with '**'
        equation_str = equation_str.replace('^', '**')
        # Parse the equation
        equation_parts = equation_str.split('=')
        result = float(equation_parts[1].strip())

        # Define the variable
        x, y = symbols('x y')

        # Define the equation
        equation = Eq(x**2 + y**2, result)

        # Solve the equation for x and y
        solutions = solve(equation, (x, y))

        return solutions
    except Exception as e:
        print(f"Error solving ellipse/hyperbola equation: {e}")
        return []

def parse_and_solve_equation(equation_str):
    try:
        equation_type = classify_equation(equation_str)
        
        if equation_type == "Linear Equation" or equation_type == "Quadratic Equation" or equation_type == "Cubic Equation" or equation_type == "Quartic Equation" or equation_type == "Rational Equation":
            solutions = solve_linearQuadraticCubicQuarticRational_equation(equation_str)
        elif equation_type == "Exponential Equation":
            solutions = solve_exponential_equation(equation_str)
        elif equation_type == "Logarithmic Equation":
            solutions = solve_logarithmic_equation(equation_str)
        elif equation_type == "Trigonometric Equation":
            solutions = solve_trigonometric_equation(equation_str)
        elif equation_type == "Radical Equation":
            solutions = solve_radical_equation(equation_str)
        elif equation_type == "Ellipse (Conic Section Equation)" or equation_type == "Hyperbola (Conic Section Equation)":
            solutions = solve_ellipseHyperbola_equation(equation_str)
        else:
            return {"error": "Unknown equation type"}
        
        return f"solution: {solutions}"
    except Exception as e:
        print(f"Error parsing and solving equation: {e}")
        return {"error": "Error processing equation"}
    
# Example usage
equation = "2 * x^2 + 3 * x - 5 = 0"
print(parse_and_solve_equation(equation))
