def perform_operation(num1: float, num2: float, operation: str) -> float or str:
    """
    Perform basic arithmetic operations on two numbers.
    
    Args:
        num1: First number (float)
        num2: Second number (float)
        operation: Operation to perform ('add', 'subtract', 'multiply', 'divide')
        
    Returns:
        Result of the operation as float, or error message for division by zero
    """
    operation = operation.lower()
    
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2
    else:
        return "Error: Invalid operation. Please choose add, subtract, multiply, or divide."
