number=int(input("Enter a number to see its multiplication table:"))
list=[1,2,3,4,5,6,7,8,9,10]
result=0
for it in list:
    result=it*number
    print(f"{number} * {it} = {result}")
    