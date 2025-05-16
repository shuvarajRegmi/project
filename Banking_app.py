class Customer:
    Bankname = "Everest Bank"

    def __init__(self, n, bal=0.0):
        self.name = n
        self.balance = bal

    def deposit(self, amt):
        self.balance += amt
        print("Current account balance is", self.balance)

    def withdraw(self, amt):
        if amt > self.balance:
            print("Insufficient funds, can't perform withdrawal at this time")
        else:
            self.balance -= amt
            print("Balance after withdrawal:", self.balance)


print("Welcome To", Customer.Bankname)

name = input("Enter your name: ")
c = Customer(name)

while True:
    print("\nChoose your Option:\n'A' → Deposit\n'B' → Withdraw\n'C' → Exit")
    option = input("Enter the option: ").lower()

    if option == 'a':
        print("Deposit Option")
        amount = float(input("Enter deposit amount: "))
        c.deposit(amount)

    elif option == 'b':
        print("Withdraw Option")
        amount = float(input("Enter withdrawal amount: "))
        c.withdraw(amount)

    elif option == 'c':
        print("Thanks for Banking with us,", name)
        break  # ← This is what stops the infinite loop!

    else:
        print("You entered an invalid option. Please try again.")

    