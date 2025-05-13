class Customer:
    Bankname="Everest Bank"
    def __init__(self,n,bal=0.0):
        self.name=n
        self.balance=bal
    def deposite(self,amt):
        self.balance=self.balance+amt
        print("Current account balance is",self.balance) 
    def withdraw(self,amt):
        if amt >self.balance:
            print("Insufficient fund can't permorm withdraw this time")
        else:
            self.balance=self.balance-amt
            print("Balance After Withdraw",self.balance)
        
        
print("Welcome To",Customer.Bankname)
name=input("Enter your name:")
c=Customer(name)
while True:
    print("Choose your Option:\n'A'---->Deposit\n'B'------>Withdraw\n'C'------>Exit")
    option=input("Enter the option:")
    if option=='a' or option=='A':
        print("Deposit Option")
        amount=float(input("Enter deopsit amount:"))
        c.deposite(amount)
    elif option =="b" or option =='B':
        print("Withdraw Option")
        amount=float(input('Enter Withdraw Amount'))
        c.withdraw(amount)
    elif option =='c' or option=='C':
        print('Thanks for Bnking',name)
    else:
        print('You enter the invalid option')
        