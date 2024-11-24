"""
# sample_code_corrected.py

This script demonstrates a corrected version of Python code designed to follow best practices. 
The code adheres to Python's PEP-8 standards, uses descriptive variable names, 
provides proper error handling, and includes type annotations.

Features:
- Consistent use of snake_case for function names.
- Descriptive variable names for better readability.
- Error handling to manage division by zero.
- Type hints for arguments and return values.
- Clear and structured main function.
"""


def calculate_sum(num1: int, num2: int) -> int:
    """Calculate the sum of two integers."""
    return num1 + num2


def divide_numbers(dividend: int, divisor: int) -> float:
    """
    Safely divide two numbers. Returns a float result.
    Handles division by zero with a custom message.
    """
    try:
        return dividend / divisor
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return float("inf")  # Return infinity to indicate error.


def main() -> None:
    """Main function to demonstrate addition and division operations."""
    num1, num2 = 5, 10
    print("Sum:", calculate_sum(num1, num2))

    dividend, divisor = 10, 0
    print("Division Result:", divide_numbers(dividend, divisor))


if __name__ == "__main__":
    main()
