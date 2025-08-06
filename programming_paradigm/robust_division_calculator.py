import sys

class DivisionCalculator:
    @staticmethod
    def safe_divide(numerator, denominator):
        """
        Safely divides two numbers with comprehensive error handling
        
        Args:
            numerator: The numerator as string (to be converted to float)
            denominator: The denominator as string (to be converted to float)
        
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

def print_usage():
    """Display usage instructions"""
    print("Division Calculator")
    print("Usage: python division_calculator.py <numerator> <denominator>")
    print("\nExamples:")
    print("  python division_calculator.py 10 5    (Normal division)")
    print("  python division_calculator.py 10 0    (Division by zero)")
    print("  python division_calculator.py ten 5   (Invalid input)")
    print("\nNote: The result will be displayed with 2 decimal places")

def main():
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