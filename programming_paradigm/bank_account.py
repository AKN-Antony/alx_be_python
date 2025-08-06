import sys

class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Add amount to the account balance"""
        if amount > 0:
            self.account_balance += amount
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        """Subtract amount from balance if sufficient funds exist"""
        if amount <= 0:
            print("Withdrawal amount must be positive")
            return False
        if self.account_balance >= amount:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Print the current account balance"""
        print(f"Current Balance: ${self.account_balance:.2f}")

def print_usage():
    """Display usage instructions"""
    print("Usage: python bank.py <command>:<amount>")
    print("Commands:")
    print("  deposit:amount  - Add money to account")
    print("  withdraw:amount - Withdraw money from account")
    print("  display         - Show current balance")
    print("\nExamples:")
    print("  python bank.py deposit:50")
    print("  python bank.py withdraw:20")
    print("  python bank.py display")

def main():
    account = BankAccount(100)  # Initialize with $100 balance
    
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)

    try:
        # Parse command and amount
        parts = sys.argv[1].split(':')
        command = parts[0].lower()
        amount = float(parts[1]) if len(parts) > 1 else None

        # Execute commands
        if command == "deposit" and amount is not None:
            account.deposit(amount)
            print(f"Deposited: ${amount:.2f}")
        elif command == "withdraw" and amount is not None:
            if account.withdraw(amount):
                print(f"Withdrew: ${amount:.2f}")
            else:
                print("Insufficient funds or invalid amount.")
        elif command == "display":
            account.display_balance()
        else:
            print("Invalid command or missing amount.")
            print_usage()

    except ValueError:
        print("Error: Amount must be a number")
        print_usage()
    except Exception as e:
        print(f"Error: {str(e)}")
        print_usage()

if __name__ == "__main__":
    main()