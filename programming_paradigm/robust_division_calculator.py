def safe_divide(numerator, denominator):
    try:
        num=float(numerator)
        den=float(denominator)
    except  ValueError:
        return print("Error: Non-numeric input provided.")
    
    try:
        result=num/den
        return result
    except ZeroDivisionError:
        return print("Error: Division by zero.")