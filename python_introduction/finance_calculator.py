## Prompting for user feedback.
monthlyIncome = float(input("Enter your monthly income:"))
monthlyExpenses = float(input("Enter your total monthly expenses:"))

##Calculating monthly savings.
monthlySavings=monthlyIncome-monthlyExpenses


##Project Annual Savings.
rate = 0.05
projectedSavings= monthlySavings * 12 + (monthlySavings*0.05)

##Output.
print ("Your monthly savings are $",monthlySavings)
print ("Projected saving after one year, with interest, is: $",projectedSavings)

