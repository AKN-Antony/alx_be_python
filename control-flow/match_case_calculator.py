# A match case calculator 
# Asks for first number 
number1 = int(input("Enter the first number: "))
# Asks for second number 
number2 = int(input("Enter the second number: "))
# Asks for the operation to be used 
operation = input("choose the operation (+, -, *, /): ")
# Perform the operation using the match case where its the user who selects the operation to be performed
match operation:
    case '+': 
        result = number1 + number2
        print("The result is:", result)
    case '-':
        result = number1 - number2
        print("The result is:", result)
    case '*':
        result = number1 * number2
        print("The result is:", result)
    case '/':
        if number2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = number1 / number2
            print("The result is:", result)
