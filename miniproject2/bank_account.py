# Bank Account Program
# Manages a customer's checking and savings account balances.

# Task 1: Define BankAccount class
class BankAccount:

    # Task 2: Define constructor with parameters to initialize instance attributes
    def __init__(self, new_name, checking_balance, savings_balance):
        self.name = new_name
        self.checking_balance = checking_balance
        self.savings_balance = savings_balance

    # Task 3: Define deposit_checking()
    def deposit_checking(self, amount):
        if amount > 0:
            self.checking_balance += amount

    # Task 4: Define deposit_savings()
    def deposit_savings(self, amount):
        if amount > 0:
            self.savings_balance += amount

    # Task 5: Define withdraw_checking()
    def withdraw_checking(self, amount):
        if amount > 0:
            if amount > self.checking_balance:
                print(f'Withdrawal of ${amount:.2f} exceeds checking balance '
                      f'of ${self.checking_balance:.2f}.')
            else:
                self.checking_balance -= amount

    # Task 6: Define withdraw_savings()
    def withdraw_savings(self, amount):
        if amount > 0:
            if amount > self.savings_balance:
                print(f'Withdrawal of ${amount:.2f} exceeds savings balance '
                      f'of ${self.savings_balance:.2f}.')
            else:
                self.savings_balance -= amount

    # Task 7: Define transfer_to_savings()
    def transfer_to_savings(self, amount):
        if amount > 0:
            self.checking_balance -= amount
            self.savings_balance += amount

    def display_info(self):
        print(f'Customer: {self.name}')
        print(f'Checking Balance: ${self.checking_balance:.2f}')
        print(f'Savings Balance: ${self.savings_balance:.2f}')


# Test program

joe = BankAccount('Joe Doe', 1000.00, 2000.00)

print('Account Information')
joe.display_info()
print()

checking_amount = float(input('Enter amount to withdraw from checking: '))
joe.withdraw_checking(checking_amount)

savings_amount = float(input('Enter amount to withdraw from savings: '))
joe.withdraw_savings(savings_amount)

joe.transfer_to_savings(300.00)

print()
print('Final Balances')
print(f'Checking Balance: ${joe.checking_balance:.2f}')
print(f'Savings Balance: ${joe.savings_balance:.2f}')
