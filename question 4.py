#Qestion 4
class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount:.2f} into account {self.account_number}. New balance: ${self.balance:.2f}")
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f} from account {self.account_number}. New balance: ${self.balance:.2f}")
        else:
            print(f"Insufficient funds in account {self.account_number}. Current balance: ${self.balance:.2f}")
    def get_balance(self):
        return self.balance
class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, interest_rate):
        super().__init__(account_number, account_holder)
        self.interest_rate = interest_rate
    def apply_interest(self):
        interest_earned = self.balance * self.interest_rate
        self.balance += interest_earned
        print(
            f"Applied {self.interest_rate * 100:.2f}% interest to account {self.account_number}. New balance: ${self.balance:.2f}")
    def __str__(self):
        return f"Account Number: {self.account_number}, Account Holder: {self.account_holder}, Balance: ${self.balance:.2f}, Interest Rate: {self.interest_rate * 100:.2f}%"
bank_account = BankAccount("937266144", "yousefsalem")
bank_account.deposit(1000)
bank_account.withdraw(500)
print(f"Final balance: ${bank_account.get_balance():.2f}")
savings_account = SavingsAccount("992577513", "mohammadsalem", 0.05)
savings_account.apply_interest()
print(savings_account)
