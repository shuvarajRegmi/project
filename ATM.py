chance=3
balance=50000
while chance>0:
    password=int(input("Enter your password"))
    if password==1234:
        print("perss 1 for balance enquiry")
        print("perss 2 for withdraw")
        print("perss 3 for cash deposit")
        x=int(input("Enter the number:"))
        if x==1:
            print(balance)
        elif x==2:
            withdraw=int(input("Enter the withdraw amount"))
            balance=balance-withdraw
            print(balance)
        elif x==3:
            cash=int(input("Enter the adding amount"))
            balance=balance+cash
            print(balance)
    elif password!=1234:
        print("enter the valid password")
        chance-=1
        