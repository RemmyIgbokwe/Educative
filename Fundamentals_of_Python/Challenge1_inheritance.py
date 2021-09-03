class Account:
    def __init__(self, title=0, balance=0):
        self.title = title
        self.balance = balance
        # write your code here
        #pass


class SavingsAccount(Account):
    def __init__(self, title=0, balance=0, interestRate=0):
        self.interestRate = interestRate
        super().__init__(title, balance)
        # write your code here
        #pass
