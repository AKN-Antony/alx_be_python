def perform_operation(num1: float, num2: float, operation: str):
    """
    Performs basic arithmetic operations with complete error checking
    
    Args:
        num1: First operand (float)
        num2: Second operand (float)
        operation: Arithmetic operation to perform (add/subtract/multiply/divide)
    
    Returns:
        Result of operation (float) or None for division by zero
    
    Raises:
        ValueError: For invalid operations
        TypeError: For non-numeric inputs
    """
    # Input validation
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise TypeError("Both operands must be numbers")
    
    operation = operation.strip().lower()
    valid_operations = ['add', 'subtract', 'multiply', 'divide']
    
    if operation not in valid_operations:
        raise ValueError(f"Invalid operation '{operation}'. Must be one of: {valid_operations}")
    
    # Perform the requested operation
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return None  # Special flag for division by zero
        return num1 / num2

def main():
    """Interactive calculator with full error handling"""
    print("Arithmetic Calculator")
    print("Operations available: add, subtract, multiply, divide")
    
    try:
        # Get and validate user input
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operation = input("Enter operation: ").strip().lower()
        
        # Perform calculation
        result = perform_operation(num1, num2, operation)
        
        # Handle results
        if result is None and operation == 'divide':
            print("Error: Division by zero is not allowed")
        else:
            print(f"Result: {result}")
    
    except ValueError as e:
        print(f"Input error: {e}")
    except TypeError as e:
        print(f"Type error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()