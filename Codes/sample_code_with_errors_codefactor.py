# sample_code_with_intentional_errors.py
# Purposefully incorrect code to trigger errors in CodeFactor

def Add(x, x):
    return x + x  # Duplicate argument names

def LoopForever():
    while True:
        pass  # Infinite loop without a break

def ComplexLogic(a, b, c):
    if a > b:
        if b > c:
            if a > c:
                return a + b + c  # Excessive nesting
