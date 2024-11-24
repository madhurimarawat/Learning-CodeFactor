"""
# sample_code_with_errors_codefactor.py

This script demonstrates an example of faulty Python code to be analyzed using CodeFactor or Codacy. 
The code contains issues like improper naming conventions, code duplication, 
and violations of Python's PEP-8 guidelines.

Issues:
- Inconsistent naming conventions.
- Code duplication.
- Lack of type hints.
- Missing error handling for division by zero.
- Unnecessarily complex or redundant logic.
"""


# Function with naming violations and redundancy
def CalculateSum(Num1, Num2):
    # Redundant logic
    result = Num1 + Num2
    return result


# Duplicate function logic
def AddTwoNumbers(Num1, Num2):
    # Redundant logic
    result = Num1 + Num2
    return result


# Function without type hints and missing error handling
def DivideNumbers(Num1, Num2):
    if Num2 == 0:  # This is flagged as overly simplistic error handling.
        return "Cannot divide by zero"
    return Num1 / Num2


# Function with inconsistent spacing and missing type hints
def MultiplyNumbers(Num1, Num2):
    Result = Num1 * Num2  # Inconsistent naming
    return Result


# Main function with improper formatting and repetition
def Main():
    print("Sum (Method 1):", CalculateSum(5, 10))
    print("Sum (Method 2):", AddTwoNumbers(5, 10))  # Duplication of logic
    print("Division Result:", DivideNumbers(10, 0))
    print("Multiplication Result:", MultiplyNumbers(5, 2))


Main()
