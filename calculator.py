# calculator.py

# def add(a, b):
#     return a + b
def add(a, b):
    try:
        return float(a) + float(b)
    except Exception:
        raise ValueError("add() only accepts numbers or numeric strings")

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
