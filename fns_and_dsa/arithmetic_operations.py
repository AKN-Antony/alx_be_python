def perform_operation(num1: float, num2: float, operation: str):
    """
    Performs basic arithmetic operations on two numbers.
    
    Args:
        num1: First number (float)
        num2: Second number (float)
        operation: The operation to perform (add/subtract/multiply/divide)
    
    Returns:
        The result of the operation (float), or None for division by zero
    
    Raises:
        ValueError: If an invalid operation is specified
    """
    operation = operation.strip().lower()
    
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        return num1 / num2 if num2 != 0 else None
    else:
        valid_ops = ['add', 'subtract', 'multiply', 'divide']
        raise ValueError(f"Invalid operation '{operation}'. Must be one of: {valid_ops}")

def main():
    """Handles user input and displays results"""
    print("Arithmetic Operations")
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()
        
        result = perform_operation(num1, num2, operation)
        
        if result is None and operation == 'divide':
            print("Error: Cannot divide by zero")
        else:
            print(f"Result: {result}")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()