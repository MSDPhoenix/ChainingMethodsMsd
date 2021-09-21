class User:
    def __init__(self,username,email_address):
        self.name = username
        self.email = email_address
        self.account_balance = 0
    def make_deposit(self,amount):
        self.account_balance += amount
        return self
    def make_withdrawal(self,amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print(self.name,"account balance",self.account_balance)
        return self
    def transfer_money(self,other_user,amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        print("Transfering",amount,"from",self.name,"to",other_user.name)
        return self

Jay = User("Jay Pritchett","jaypritchett@Pritchettsclosets.com")
Gloria = User("Gloria Pritchett","spicycolumbian@gmail.com")
Claire = User("Claire Dunphy","toomanytequilas@yahoo.com")

Jay.make_deposit(1200).make_deposit(1000).make_deposit(1000).make_withdrawal(330).display_user_balance()

Gloria.make_deposit(1000).make_deposit(1000).make_withdrawal(330).make_withdrawal(330).display_user_balance()

Claire.make_deposit(1000).make_withdrawal(330).make_withdrawal(330).make_withdrawal(330).display_user_balance()

Jay.transfer_money(Claire,500).display_user_balance()
Claire.display_user_balance()
