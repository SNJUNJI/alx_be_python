## Prompting for user feedback.
Monthly_Income = float(input("Enter your monthly income:"))
Monthly_Expenses = float(input("Enter your total monthly expenses:"))

##Calculating monthly savings.
Monthly_Savings=Monthly_Income-Monthly_Expenses


##Project Annual Savings.
rate = 0.05
Projected_Savings = Monthly_Savings * 12 + (Monthly_Savings*0.05)

##Output.
print ("Your monthly savings are $",Monthly_Savings)
print ("Projected saving after one year, with interest, is: $",Projected_Savings)

