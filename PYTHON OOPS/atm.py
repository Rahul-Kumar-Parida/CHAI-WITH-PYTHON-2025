class Account:
    def __init__(self, name, account_number, pin, balance=0.0):
        self.name = name
        self.account_number = account_number
        self.pin = pin
        self.balance = balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            return True
        return False

    def transfer(self, amount, recipient):
        if self.withdraw(amount):
            recipient.deposit(amount)
            return True
        return False

class ATM:
    def __init__(self):
        self.accounts = [
            Account("John Doe", "1001", "1234", 5000.0),
            Account("Jane Smith", "1002", "5678", 10000.0)
        ]
        self.current_user = None

    def authenticate(self):
        account_number = input("Enter account number: ")
        pin = input("Enter PIN: ")

        for account in self.accounts:
            if account.account_number == account_number and account.pin == pin:
                self.current_user = account
                print("\nAuthentication successful!")
                return
        print("\nAuthentication failed. Invalid credentials.")
        self.current_user = None

    def display_menu(self):
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Logout")
        print("6. Exit")

    def run(self):
        while True:
            if not self.current_user:
                self.authenticate()
            else:
                self.display_menu()
                choice = input("Enter choice (1-6): ")

                if choice == "1":
                    print(f"\nBalance: ${self.current_user.check_balance():.2f}")

                elif choice == "2":
                    self.process_deposit()

                elif choice == "3":
                    self.process_withdrawal()

                elif choice == "4":
                    self.process_transfer()

                elif choice == "5":
                    self.current_user = None
                    print("\nLogged out successfully!")

                elif choice == "6":
                    print("\nThank you for using our ATM!")
                    exit()

                else:
                    print("\nInvalid choice. Try again.")

    def process_deposit(self):
        try:
            amount = float(input("Enter deposit amount: $"))
            if amount > 0 and self.current_user.deposit(amount):
                print(f"Deposited ${amount:.2f}. New balance: ${self.current_user.check_balance():.2f}")
            else:
                print("Invalid deposit amount.")
        except ValueError:
            print("Invalid input. Please enter numbers only.")

    def process_withdrawal(self):
        try:
            amount = float(input("Enter withdrawal amount: $"))
            if self.current_user.withdraw(amount):
                print(f"Withdrew ${amount:.2f}. New balance: ${self.current_user.check_balance():.2f}")
            else:
                print("Insufficient funds or invalid amount.")
        except ValueError:
            print("Invalid input. Please enter numbers only.")

    def process_transfer(self):
        recipient_number = input("Enter recipient's account number: ")
        recipient = next((acc for acc in self.accounts if acc.account_number == recipient_number), None)
        
        if recipient:
            try:
                amount = float(input("Enter transfer amount: $"))
                if self.current_user.transfer(amount, recipient):
                    print(f"Transferred ${amount:.2f} to {recipient.name}. Your balance: ${self.current_user.check_balance():.2f}")
                else:
                    print("Transfer failed. Check balance and amount.")
            except ValueError:
                print("Invalid input. Please enter numbers only.")
        else:
            print("Recipient account not found.")

if __name__ == "__main__":
    atm = ATM()
    atm.run()