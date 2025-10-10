def safe_divide(numerator, denominator):
    try:
        num=float(numerator)
        den=float(denominator)
    except  ValueError:
        return "Error: Non-numeric input provided."
    
    try:
        result=num/den
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."