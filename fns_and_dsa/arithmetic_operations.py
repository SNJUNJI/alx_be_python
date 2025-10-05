def perform_operation(num1, num2, operation):

    if operation == "add":
        return num1+num2 
    if operation=="subtract":
        return num1-num2
    if operation=="multiply":
        return num1*num2
    if operation == "divide":
        if num1 == 0 or num2 == 0:
            print("ERROR-Division by Zero. ")
        else:
            return num1/num2
        