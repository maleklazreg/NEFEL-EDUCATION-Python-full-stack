class BankAccount:
    def __init__(self, balanceamount = 0, interest = 0.01):
        self.balancamount = balanceamount
        self.interest = interest

    def deposit(self, amount):
        self.balancamount = self.balancamount + amount
        return self
    
    def withdraw(self, amount):
        if self.balancamount - amount < 0:
            print("Charging a $5 fee and deduct $5")
        else:
            self.balancamount = self.balancamount - amount
        return self

    
    def display_user_balance(self):
        print(f"Balance: {self.balancamount}")
        return self
    
    def yield_interest(self):
        if self.balancamount > 0:
            self.balancamount = self.balancamount + (self.balancamount * self.interest)
        return self
    
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(interest = 0.02, balancamount = 0)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        self.account.balance_amount = amount

    def make_withdraw(self, amount):
        if self.account.balancamount - amount < 0:
            print("Charging a $5 fee and deduct $5")
        else:
            self.account.balancamount = self.account.balancamount - amount

    def display_user_balance(self):
        print("Balance:",self.account.balancamount)

user1 = User("lzareg", "lazregmalek30@gmail.com")
user2 = User("lzareg", "lazregmalek30@gmail.com")

user1.make_deposit(1000)

user1.make_withdraw(500)

user1.display_user_balance()

user2.display_user_balance()
        