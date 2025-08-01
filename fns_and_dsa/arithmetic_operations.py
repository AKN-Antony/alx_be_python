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
    operations = {
        'add': lambda a, b: a + b,
        'subtract': lambda a, b: a - b,
        'multiply': lambda a, b: a * b,
        'divide': lambda a, b: a / b if b != 0 else None
    }
    
    operation = operation.strip().lower()
    
    if operation not in operations:
        valid_operations = list(operations.keys())
        raise ValueError(f"Invalid operation '{operation}'. Must be one of: {valid_operations}")
    
    return operations[operation](num1, num2)

# Test code that runs when the script is executed directly
if __name__ == "__main__":
    print("Testing arithmetic_operations.py")
    
    test_cases = [
        (5, 3, 'add', 8),
        (10, 4, 'subtract', 6),
        (7, 2, 'multiply', 14),
        (8, 2, 'divide', 4),
        (5, 0, 'divide', None),
        (10, 3, 'power', None)  # Should raise ValueError
    ]
    
    for num1, num2, op, expected in test_cases:
        try:
            result = perform_operation(num1, num2, op)
            print(f"{num1} {op} {num2} = {result} (Expected: {expected})")
        except ValueError as e:
            print(f"{num1} {op} {num2} = Error: {e}")