"""
# sample_code_with_errors_codefactor.py

This script demonstrates faulty Python code designed to trigger errors in code quality analysis tools.
It includes major issues such as:
- Functions with duplicate names.
- Poor indentation.
- Code duplication.
- Missing type hints.
- Improper variable naming conventions.
"""

# Function with duplicate names
def CalculateSum(Num1, Num2):
result = Num1 + Num2
return result

# Duplicate function name with different logic
def CalculateSum(Num1, Num2):
result = Num1 * Num2
return result

# Function with poor formatting and no type hints
def divideNumbers (Num1,Num2):
    if Num2==0:
     return"Cannot divide by zero"
    return Num1/Num2

# Another function with poor formatting and unnecessary nesting
def ComplexLogic(A,B,C):
if A>B:
      if B>C:
  if A>C:
          return A+B+C
else:
  return 0

# Function with redundant code and inconsistent variable naming
def multiply_two_numbers(num1,num2):
    product = num1*num2
    return product
def multiply_two_numbers(num1,num2):
    # Duplicate function body
 product = num1*num2
 return product

# Main function with significant formatting and redundancy issues
def Main ( ) :
print( "Sum (Method 1):", CalculateSum(5,10))
print("Sum (Method 2):",CalculateSum(5,10)) # Duplication of logic
print ("Division Result:" , divideNumbers ( 10 ,0 ) )
    print("Multiplication:", multiply_two_numbers(5,2))
print("Redundant Multiplication:",multiply_two_numbers(5,2)) # Duplication
