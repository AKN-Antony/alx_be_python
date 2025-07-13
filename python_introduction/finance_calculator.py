income = int(input("Enter your monthly income:"))

expenses = int(input("Enter your monthly expenses:"))

savings = income - expenses

interest = 0.05

Projected_Savings = savings * 12 + (savings * 12 * 0.05)

print("your monthly savings are :", savings)
print("Projected savingd after one year, with interest, is :", Projected_Savings)

