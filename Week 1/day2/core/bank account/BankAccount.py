class bankaccount:
    all_accounts = []

    def __init__(self, intrate=0.01, balance=0):
        self.intrate = intrate
        self.balance = balance
        bankaccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def deisplayaccount(self):
        print(f"Balance: ${self.balance}")
        return self

    def yieldinterest(self):
        if self.balance > 0:
            #self.balance += (self.balance * self.int_rate)
            interest = self.balance * self.intrate
            self.balance += interest
        return self.balance

    @classmethod
    def printallaccounts(cls):
        for account in cls.all_accounts:
            account.displayaccount()
        return self

acc1 = bankaccount(0.02, 1000)
acc1.deposit(500).withdraw(200).yieldinterest()


acc2 = bankaccount(0.03, 2000)
acc2.deposit(1000).withdraw(500).withdraw(500).withdraw(500).withdraw(500).yieldinterest()

bankaccount.printallaccounts()

        
