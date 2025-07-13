income = int(input("Enter your monthly income:"))

expenses = int(input("Enter your monthly expenses:"))

savings = income - expenses

interest = 0.05

Projected_Savings = savings * 12 + (savings * 12 * interest)

print("your monthly savings are :", savings)
print("Projected savings after one year, with interest, is :", Projected_Savings)

