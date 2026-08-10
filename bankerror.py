class InvalidBalanceError(Exception):
    pass

class bankaccount:
    def __init__(self,balance):
        self.balance = balance
    def withdraw(self,amount):
        if amount > self.balance:
            raise InvalidBalanceError(
                "Insufficient balance"
            )
        self.balance == amount
        print("Withdrawal successful")

account = bankaccount(5000)
try:
    account.withdraw(6000)

except InvalidBalanceError as e:
    print("Error : ",e)