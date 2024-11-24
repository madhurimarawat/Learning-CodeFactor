"""
# sample_code_with_errors.py

This script demonstrates an example of faulty Python code to be analyzed using CodeFactor or Codacy. 
The code contains issues like improper naming conventions, lack of error handling, 
and violations of Python's PEP-8 guidelines.

Issues:
- Inconsistent indentation levels.
- Missing error handling for division by zero.
- Non-descriptive variable names.
- Violation of snake_case for function naming.
- Lack of type hints.
"""


def calculateSum(Num1, Num2):
    return Num1 + Num2


def divideNumbers(num1, num2):
    result = num1 / num2
    return result


def main():
    print("Sum: ", calculateSum(5, 10))
    print("Division Result:", divideNumbers(10, 0))


main()
