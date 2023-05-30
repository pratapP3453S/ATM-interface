import sys
import os


def atm_running():
    class ATM():
        bankname = "PRATAP BANKING"
        welcome = f"\t\t\t***** WELCOME TO {bankname} APPLICATION *****"
        avail_balance = 0

        def __init__(self, name):
            self.name = name
            self.balance_in_acc()
            self.balance = self.avail_balance

        def balance_in_acc(self):
            with open("avail_balance_money", "r") as file:
                self.avail_balance = file.readline()

        def withdraw(self):
            with open("avail_balance_money", "r") as file:
                amout_in_acc = int(file.readline())
            user_amount = int(input("Enter Withdraw Amount : "))
            if user_amount > amout_in_acc:
                print("Insufficent balance....")
                sys.exit()
            else:
                subtract_amount = amout_in_acc - user_amount
                with open("avail_balance_money", "w") as input_file:
                    input_file.write(str(subtract_amount))
                input_file.close()
                print(f"Available Balance Is : {subtract_amount} rupees")

        def deposit(self):
            with open("avail_balance_money", "r") as file:
                amount_in_acc = int(file.readline())
            user_amount = int(input("Enter Deposit Amount : "))
            adding_amount = amount_in_acc + user_amount
            with open("avail_balance_money", "w") as input_file:
                input_file.write(str(adding_amount))
            input_file.close()
            print(f"Available Balance Is : {adding_amount} rupees")

        def check_balance(self):
            print(f"Available Balance : {self.avail_balance} rupees")

        def exit_app(self):
            print("Thank You For Coming.")
            sys.exit()

    print(ATM.welcome)
    name = str(input("enter your name on account : "))
    obj = ATM(name)
    customer = 0
    while (True):
        print("\nw for withdraw\nd for deposit\nc for check balance\nc for check balance\ne for exit")
        cust_work = str(input("enter the option : "))
        if cust_work == "w":
            obj.withdraw()
        elif cust_work == "d":
            obj.deposit()
        elif cust_work == "c":
            obj.check_balance()
        elif cust_work == "e":
            obj.exit_app()
        else:
            print("invalid option selected...")
            sys.exit()
        customer = str(
            input("are you want to use this application again = YES | NO : "))
        if customer == "no":
            print("Thank You For Coming.")
            sys.exit()


if os.path.isfile("avail_balance_money"):
    atm_running()
else:
    with open("avail_balance_money", "w") as file:
        file.write("100")
        print("hey you just won a welcome amount of 100 rupees, credited to your account\
              now your account balance is 100 rupees *._.*")
        atm_running()


