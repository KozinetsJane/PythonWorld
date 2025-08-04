import random

class BankAccount:
    def __init__(self, balance, account_number):
        if balance < 0:
            raise ValueError("Начальный баланс не может быть меньше нуля")
        self.__balance = balance
        self.__account_number = account_number

    @property
    def balance(self):
        return self.__balance
    @property
    def account_number(self):
        return self.__account_number
    
    @balance.setter
    def balance(self, value):
        if value >= 0:
            self.__balance = value
        else:
            raise ValueError("Баланс не может быть отрицательным")

    @staticmethod
    def generate_account_number():
        return ''.join(str(random.randint(0, 9)) for _ in range(10))
    
    @classmethod
    def create_account(cls, initial_balance):
        acc_num = cls.generate_account_number()
        return cls(initial_balance, acc_num)

myaccount1 = BankAccount.create_account(1000)
print("Account Number:", myaccount1.account_number)
print("Balance:", myaccount1.balance)


try:
    myaccount1.balance = -100
except ValueError as e:
    print("Error:", e)
