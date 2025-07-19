number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
operation = input("choose the operation (+, -, *, /): ")
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
