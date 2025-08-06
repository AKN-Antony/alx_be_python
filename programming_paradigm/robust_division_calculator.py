import sys

class DivisionCalculator:
    @staticmethod
    def safe_divide(numerator, denominator):
        """
        Safely divides two numbers with comprehensive error handling
        
        Args:
            numerator: The numerator (string or number)
            denominator: The denominator (string or number)
        
        Returns:
            str: Result message or error message
        """
        try:
            # Convert inputs to floats
            num = float(numerator)
            den = float(denominator)
            
            # Check for division by zero
            if den == 0:
                return "Error: Cannot divide by zero."
                
            # Perform division and format result
            result = num / den
            return f"The result of the division is {result:.2f}"
        
        except ValueError:
            return "Error: Please enter numeric values only."
        
        except Exception as e:
            return f"Error: An unexpected error occurred - {str(e)}"

def run_tests():
    """Run automated tests to verify correct outputs"""
    test_cases = [
        # (numerator, denominator, expected_output)
        ("10", "5", "The result of the division is 2.00"),
        ("10", "0", "Error: Cannot divide by zero."),
        ("ten", "5", "Error: Please enter numeric values only."),
        ("7.5", "2", "The result of the division is 3.75"),
        ("15", "three", "Error: Please enter numeric values only."),
    ]
    
    print("Running tests...")
    failures = 0
    
    for i, (num, den, expected) in enumerate(test_cases, 1):
        result = DivisionCalculator.safe_divide(num, den)
        if result == expected:
            print(f"✓ Test {i}: PASSED")
        else:
            print(f"✗ Test {i}: FAILED")
            print(f"   Input: {num}/{den}")
            print(f"   Expected: {expected}")
            print(f"   Got: {result}")
            failures += 1
    
    if failures == 0:
        print("All tests passed successfully!")
    else:
        print(f"\n{failures} tests failed")
    
    return failures

def print_usage():
    """Display usage instructions"""
    print("Division Calculator")
    print("Usage: python division_calculator.py <numerator> <denominator>")
    print("       python division_calculator.py --test (to run tests)")
    print("\nExamples:")
    print("  python division_calculator.py 10 5")
    print("  python division_calculator.py 10 0")
    print("  python division_calculator.py ten 5")

def main():
    # Check for test mode
    if len(sys.argv) == 2 and sys.argv[1] == "--test":
        sys.exit(run_tests())
    
    # Check for correct number of arguments
    if len(sys.argv) != 3:
        print_usage()
        sys.exit(1)
    
    # Get arguments from command line
    numerator = sys.argv[1]
    denominator = sys.argv[2]
    
    # Perform safe division and print result
    result = DivisionCalculator.safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()