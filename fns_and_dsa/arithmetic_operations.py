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
    # Dictionary mapping operations to their corresponding functions
    operations = {
        'add': lambda a, b: a + b,
        'subtract': lambda a, b: a - b,
        'multiply': lambda a, b: a * b,
        'divide': lambda a, b: a / b if b != 0 else None
    }
    
    # Normalize the operation string (lowercase and strip whitespace)
    operation = operation.strip().lower()
    
    # Check if the operation is valid
    if operation not in operations:
        valid_operations = ', '.join(operations.keys())
        raise ValueError(f"Invalid operation '{operation}'. Must be one of: {valid_operations}")
    
    # Perform the operation
    result = operations[operation](num1, num2)
    
    return result