number=int(input("Enter a number to see its multiplication table:"))
result=0
for it in range(1,11):
    result=it*number
    print(f"{number} * {it} = {result}")
