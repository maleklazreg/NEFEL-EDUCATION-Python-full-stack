class BankAccount:
    def __init__(self, name, email,):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

    def make_deposit(self, amount):
        self.balence += amount
        return self
    
    def make_withdraw(self, amount):
        if self.display_balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")
        return self

    
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account.balance}")
        return self
        