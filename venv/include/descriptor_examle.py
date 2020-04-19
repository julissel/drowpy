from datetime import datetime


class ImportantValue:
    def __init__(self, amount):
        self.amount = amount

    def __get__(self, obj, obj_type):
        return self.amount

    def __set__(self, obj, value):
        with open('log_descriptor.txt', 'a') as f:
            f.writelines([f"{datetime.utcnow()} old: {self.amount}", "\n", f"{datetime.utcnow()} new: {value}", "\n"])
        self.amount = value


class Account:
    amount = ImportantValue(100)


client_account = Account()
client_account.amount = 200


with open('log_descriptor.txt', 'r') as f:
    print(f.read())
