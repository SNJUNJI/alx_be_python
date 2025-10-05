def perform_operation(num1,num2,operation):
    num1=float(input("Enter the first number: "))
    num2=float(input("Enter the second number: "))
    operation=str(input("Enter operation"))

    if operation == "add":
        result=num1+num2
        return result
    if operation=="subtract":
        result=num1-num2
        return result
    if operation=="multiply":
        result=num1*num2
        return result
    if operation == "divide":
        if num1 == 0 or num2 == 0:
            print("ERROR-Division by Zero. ")
        else:
            result=num1/num2
            return result
        