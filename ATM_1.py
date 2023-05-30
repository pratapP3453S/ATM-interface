from tkinter import *
import time
from tkinter import messagebox as mb
import os

class ATM():
    bankname = "PRATAP BANKING"
    avail_balance = 0

    def __init__(self):
        self.check_locker()
        self.balance = self.avail_balance
    def check_locker(self):
        if os.path.isfile("avail_balance_money"):
            self.balance_in_acc()
        else:
            # print("\nfree 100 rupees added to your account for first opening")
            with open("avail_balance_money", "w") as file:
                file.write("100")
            self.new_account()
    def testing_4(self):
        self.choose = mb.showinfo("Reward","As A New Customer Free 100 rupees credited to your account!")
        if self.choose == "yes":
            main()
    def new_account(self):
        self.rootna = Toplevel()
        self.rootna.geometry("1276x710")
        self.rootna.title("ACCOUNT-DEBIT CARD")
        self.photo = PhotoImage(file=r"C:\Users\abc\Pictures\Screenshots\Annotation 2023-04-24 151733main.png")
        self.lab = Label(self.rootna,image=self.photo)
        self.lab.place(x=0,y=0)    
        self.title = Label(self.rootna,text="***You Have Won A Reward***",fg="dark blue",\
                           font=("Arial Black",30))
        self.title.pack(anchor=CENTER,side=TOP)
        self.button = Button(self.rootna,text="OK",bd='5',height=2,width=20,font="Algerian",fg="black",\
                  bg="dark blue",command=self.testing_4)
        self.button.pack(pady=10,anchor=CENTER,side=BOTTOM)
        self.rootna.mainloop()
    def balance_in_acc(self):
        with open("avail_balance_money", "r") as file:
            self.avail_balance = file.readline()
        
    def testing_1(self):
        self.choose = mb.askquestion("Confirm","Are You Sure...Want To Return Home Page!")
        if self.choose == "yes":
            main
        else:
            self.withdraw()
    def testing_2(self):
        self.choose = mb.askquestion("Confirm","Are You Sure...Want To Return Home Page!")
        if self.choose == "yes":
            main
        else:
            self.deposit()
    def testing_3(self):
        self.choose = mb.askquestion("Confirm","Are You Sure...Want To Return Home Page!")
        if self.choose == "yes":
            main
        else:
            TransactionType()
    def testing_5(self):
        self.choose = mb.askquestion("Confirm","Are You Sure...Want To Return Home Page!")
        if self.choose == "yes":
            main
        else:
            PinVerification1()

    def withdraw(self):
        self.root1c = Toplevel()
        self.root1c.geometry("1276x710")
        self.root1c.title("ATM-ProcessMenu")
        self.photo = PhotoImage(file=r"C:\Users\abc\Pictures\Screenshots\Annotation 2023-04-24 152212main.png")
        self.lab = Label(self.root1c,image=self.photo)
        self.lab.place(x=0,y=0)  
        self.title = Label(self.root1c,text="Enter Withdraw Amount !",fg="dark blue",font=("Arial Black",34))
        self.title.pack(anchor=CENTER,side=TOP)
        self.entry = Entry(self.root1c,width=100)
        self.entry.pack(pady=20,padx=20,anchor=CENTER,side=TOP)
        self.buttoncc = Button(self.root1c,text="Cancel",bd='5',height=2,width=20,font="Algerian",fg="black",\
                     bg="dark blue",command=self.testing_1)
        self.buttoncc.pack(pady=50,anchor=CENTER,side=BOTTOM)
        self.button = Button(self.root1c,text="OK",bd='5',height=2,width=20,font="Algerian",fg="black",\
                     bg="dark blue",command=self.collecting_cash)
        self.button.pack(pady=25,anchor=CENTER,side=TOP)
    def collecting_cash(self):
        value = float(self.entry.get())
        with open("avail_balance_money", "r") as file:
            amount_in_acc = float(file.readline())
        if value%10==0:
            if value > amount_in_acc:
               cust = mb.showinfo("Insufficent balance","Insufficent Balance....!")
               if cust == "ok":
                    # print("Thank You For Coming.")
                    main
            elif value < 100:
               custm = mb.showerror("Low-Cash","You Can't Withdraw Cash Less Than 100 rs!")
               if custm == "ok":
                    self.withdraw()       
            else:
                self.subtract_amount = amount_in_acc - value
                with open("avail_balance_money", "w") as input_file:
                    input_file.write(str(self.subtract_amount))
                input_file.close()
                self.collect_cash()
        else:
            custm1 = mb.showerror("Low-Cash","You Only Withdraw Cash Multiple of 10!")
            if custm1 == "ok":
                 self.withdraw()             
    def collect_cash(self):
        time.sleep(2)
        self.clicking = mb.showinfo("Collect Cash",f"Please Collect Your cash And Remove Your Card \
                               \nYour Available Balance Is : {self.subtract_amount} Rupees.")
        if self.clicking == "ok":
            main
            
            # print(f"Available Balance Is : {subtract_amount} rupees")

    def deposit(self):
        self.root1c = Toplevel()
        self.root1c.geometry("1276x710")
        self.root1c.title("ATM-ProcessMenu")
        self.photo = PhotoImage(file=r"C:\Users\abc\Pictures\Screenshots\Annotation 2023-04-24 152334main.png")
        self.lab = Label(self.root1c,image=self.photo)
        self.lab.place(x=0,y=0)
        self.title = Label(self.root1c,text="Enter Deposit Amount !",fg="dark blue",font=("Arial Black",34))
        self.title.pack(anchor=CENTER,side=TOP)
        self.entry = Entry(self.root1c,width=100)
        self.entry.pack(pady=20,padx=20,anchor=CENTER,side=TOP)
        
        self.buttoncc = Button(self.root1c,text="Cancel",bd='5',height=2,width=20,font="Algerian",fg="black",\
                     bg="dark blue",command=self.testing_2)
        self.buttoncc.pack(pady=50,anchor=CENTER,side=BOTTOM)
        self.button = Button(self.root1c,text="OK",bd='5',height=2,width=20,font="Algerian",fg="black",\
                     bg="dark blue",command=self.depositing_cash)
        self.button.pack(pady=25,anchor=CENTER,side=TOP)
    def depositing_cash(self):
        value = float(self.entry.get())
        with open("avail_balance_money", "r") as file:
            amount_in_acc = float(file.readline())
        self.adding_amount = amount_in_acc + value
        with open("avail_balance_money", "w") as input_file:
            input_file.write(str(self.adding_amount))
        input_file.close()
        self.showing_balance()
    def showing_balance(self):
        time.sleep(2)
        self.clicked = mb.showinfo("Cash Deposited",f"Cash Deposited Now Remove Your Card \
                               \nYour Available Balance Is : {self.adding_amount} Rupees.")
        if self.clicked == "ok":
            main
    def check_balance(self):
        self.root2c = Toplevel()
        self.root2c.geometry("1276x710")
        self.root2c.title("ATM-ProcessMenu")
        self.photo = PhotoImage(file=r"C:\Users\abc\Pictures\Screenshots\Annotation 2023-04-24 151317main.png")
        self.lab = Label(self.root2c,image=self.photo)
        self.lab.place(x=0,y=0)
        self.title = Label(self.root2c,text="Available Balance In Account !",fg="dark blue",font=("Arial Black",34))
        self.title.pack(anchor=CENTER,side=TOP)
        self.title2 = Label(self.root2c,text=f"Available Balance In Your Account Is : "\
                            ,fg="red",font=("Arial Black",34))
        self.title3 = Label(self.root2c,text=f"{self.avail_balance} rupees.",fg="black"\
                            ,font=("Arial Black",34))
        self.button = Button(self.root2c,text="OK",bd='5',height=2,width=20,font="Algerian",fg="black",\
                     bg="dark blue",command=self.root2c.destroy)
        self.title2.pack(pady=25,anchor=CENTER,side=TOP)
        self.title3.pack(anchor=CENTER,side=TOP)
        self.button.pack(pady=25,anchor=CENTER,side=BOTTOM)          
    def update_pin():
        pass
    def money_transfer():
        pass
    def show_account():
        pass
    def net_banking():
        pass
def testing_5a():
    choose = mb.askquestion("Confirm","Are You Sure...Want To Return Home Page!")
    if choose == "yes":
        main
    else:
        English()
def generate_pin():
    root2a = Toplevel()
    root2a.geometry("1276x710")
    root2a.title("ACCOUNT-Generator")
    photo = PhotoImage(file=r"C:\Users\abc\Pictures\Screenshots\Annotation 2023-04-24 152334main.png")
    lab = Label(root,image=photo)
    lab.place(x=0,y=0)
    title = Label(root2a,text="Generate Your New PIN!",fg="dark blue",font=("Arial Black",34))
    title.pack(anchor=CENTER,side=TOP) 
    entry1 = Entry(root2a,show="*",width=100)
    entry1.pack(pady=20,padx=20,anchor=CENTER,side=TOP)
    entry1.focus()
    button = Button(root2a,text="OK",bd='5',height=2,width=20,font="Algerian",fg="black",\
                 bg="dark blue")
    button.pack(pady=20,anchor=CENTER,side=TOP)
    entry2 = Entry(root2a,show="*",width=100)
    entry2.pack(pady=20,padx=10,anchor=CENTER,side=TOP)
    def check_both():
        try:
            firstpin_value = int(entry1.get())
            secondpin_value = int(entry2.get())
            if firstpin_value == secondpin_value:
                
                with open("new_pin_code","w") as file:
                    file.write(str(firstpin_value))
                choose = mb.showinfo("PIN-Generator","PIN Generated Successfully...!")
                if choose == "ok":
                    main
            else:
                choosing = mb.showerror("Error","Both PIN Not Matched...")
                if choosing == "ok":
                    main
        except:
            time.sleep(2)
            choose = mb.showerror("Wrong-PIN","Provided PIN Is Wrong...!")
            if choose == "yes":
                main
    button2 = Button(root2a,text="Confirm Pin",bd='5',height=2,width=20,font="Algerian",fg="black",\
                 bg="dark blue",command=check_both)
    button2.pack(pady=10,anchor=CENTER,side=TOP)
    button3 = Button(root2a,text="Cancel",bd='5',height=2,width=20,font="Algerian",fg="black",\
                 bg="dark blue",command=root2a.destroy)
    button3.pack(pady=10,anchor=CENTER,side=BOTTOM)
def not_release():
    pass



def TransactionType():
    root4 = Toplevel()
    obj = ATM()
    root4.geometry("1276x710")
    root4.title("ATM-ProcessMenu")
    photo = PhotoImage(file=r"C:\Users\abc\Pictures\Screenshots\Annotation 2023-04-24 151802main1.png")
    lab = Label(root4,image=photo)
    lab.place(x=0,y=0)
    frame = Frame(root4)
    title = Label(root4,text="Select Transaction Type !",fg="dark blue",font=("Arial Black",34))
    title.pack(anchor=CENTER,side=TOP)
    button1 = Button(frame,text="Withdraw Cash",bd='5',height=2,width=20,font="Algerian",fg="black",\
                     bg="dark blue",command=PinVerification1)
    button2 = Button(frame,text="Deposit Cash",bd='5',height=2,width=20,font="Algerian",fg="black",\
                     bg="dark blue",command=PinVerification2)
    button3 = Button(frame,text="Check Balance",bd='5',height=2,width=20,font="Algerian",fg="black",\
                     bg="dark blue",command=PinVerification3)
    button4 = Button(frame,text="Generate New PIN",bd='5',height=2,width=20,font="Algerian",fg="black",\
                     bg="dark blue",command=generate_pin)
    button1.pack(pady=20)
    button2.pack(pady=20)
    button3.pack(pady=20)
    button4.pack(pady=20)
    frame.pack(pady=20,anchor=CENTER,side=RIGHT)
    frame2 = Frame(root4)
    button5 = Button(frame2,text="Update PIN",bd='5',height=2,width=20,font="Algerian",fg="black",\
                     bg="dark blue",command=obj.update_pin)
    button6 = Button(frame2,text="Money Transfer",bd='5',height=2,width=20,font="Algerian",fg="black",\
                     bg="dark blue",command=obj.money_transfer)
    button7 = Button(frame2,text="Net Banking",bd='5',height=2,width=20,font="Algerian",fg="black",\
                     bg="dark blue",command=obj.net_banking)
    button8 = Button(frame2,text="Show ACCOUNT",bd='5',height=2,width=20,font="Algerian",fg="black",\
                     bg="dark blue",command=obj.show_account)
    button5.pack(pady=20)
    button6.pack(pady=20)
    button7.pack(pady=20)
    button8.pack(pady=20)
    frame2.pack(pady=20,anchor=CENTER,side=LEFT)

    button9 = Button(root4,text="Cancel",bd='5',height=2,width=20,font="Algerian",fg="black",\
                     bg="dark blue",command=obj.testing_3)
    button9.pack(pady=20,anchor=CENTER,side=BOTTOM)
    root4.mainloop()
def to_home():
    time.sleep(2)
    choose = mb.showerror("Wrong-PIN","Provided PIN Is Wrong...!")
    if choose == "ok":
        main 
def PinVerification3():
    time.sleep(2)
    root3 = Toplevel()
    obj = ATM()
    root3.geometry("1276x710")
    root3.title("ATM-PIN")
    photo = PhotoImage(file=r"C:\Users\abc\Pictures\Screenshots\Annotation 2023-04-24 152144main.png")
    lab = Label(root3,image=photo)
    lab.place(x=0,y=0)
    title = Label(root3,text="Please Enter Your CARD Pin !",fg="dark blue",font=("Arial Black",34))
    title.pack(anchor=CENTER,side=TOP)
    button9 = Button(root3,text="Cancel",bd='5',height=2,width=20,font="Algerian",fg="black",\
                     bg="dark blue",command=obj.testing_5)
    button9.pack(pady=20,anchor=CENTER,side=BOTTOM)
    enterpin = Entry(root3,show="*",width=100)
    enterpin.pack(pady=17,anchor=CENTER,side=TOP)
    def input_value():
        try:
            with open("new_pin_code","r") as file:
                pin_value = int(file.readline())
            value = int(enterpin.get())
            if value == pin_value:
                time.sleep(2)
                choose = mb.showinfo("PIN-Vefied","PIN Verified Successfully!")
                if choose == "ok":
                    obj.check_balance()
            else:
                to_home()
        except:
            to_home()
    button9u = Button(root3,text="Ok",bd='5',height=2,width=20,font="Algerian",fg="black",\
                     bg="dark blue",command=input_value)
    button9u.pack(pady=20,anchor=CENTER,side=RIGHT)
    root3.mainloop()
def PinVerification2():
    time.sleep(2)
    root3 = Toplevel()
    obj = ATM()
    root3.geometry("1276x710")
    root3.title("ATM-PIN")
    photo = PhotoImage(file=r"C:\Users\abc\Pictures\Screenshots\Annotation 2023-04-24 152144main.png")
    lab = Label(root3,image=photo)
    lab.place(x=0,y=0)
    title = Label(root3,text="Please Enter Your CARD Pin !",fg="dark blue",font=("Arial Black",34))
    title.pack(anchor=CENTER,side=TOP)
    button9 = Button(root3,text="Cancel",bd='5',height=2,width=20,font="Algerian",fg="black",\
                     bg="dark blue",command=obj.testing_5)
    button9.pack(pady=20,anchor=CENTER,side=BOTTOM)
    enterpin = Entry(root3,show="*",width=100)
    enterpin.pack(pady=17,anchor=CENTER,side=TOP)
    def account_type2():
        root4 = Toplevel()
        root4.geometry("1276x710")
        root4.title("ATM-Account Type")
        photo = PhotoImage(file=r"C:\Users\abc\Pictures\Screenshots\Annotation 2023-04-24 151733main.png")
        lab = Label(root4,image=photo)
        lab.place(x=0,y=0)
        frame = Frame(root4)
        title = Label(root4,text="Select Transaction Type !",fg="dark blue",font=("Arial Black",34))
        title.pack(anchor=CENTER,side=TOP)
        button1 = Button(frame,text="Current Account",bd='5',height=2,width=20,font="Algerian",fg="black",\
                         bg="dark blue",command=obj.deposit)
        button2 = Button(frame,text="Saving Account",bd='5',height=2,width=20,font="Algerian",fg="black",\
                         bg="dark blue",command=obj.deposit)
        button3 = Button(frame,text="Salary Account",bd='5',height=2,width=20,font="Algerian",fg="black",\
                         bg="dark blue",command=obj.deposit)
        button4 = Button(frame,text="NRI Account",bd='5',height=2,width=20,font="Algerian",fg="black",\
                         bg="dark blue",command=not_release)
        button1.pack(pady=20)
        button2.pack(pady=20)
        button3.pack(pady=20)
        button4.pack(pady=20)
        frame.pack(pady=20,anchor=CENTER,side=RIGHT)
    def input_value():
        try:
            with open("new_pin_code","r") as file:
                pin_value = int(file.readline())
            value = int(enterpin.get())
            if value == pin_value:
                time.sleep(2)
                choose = mb.showinfo("PIN-Vefied","PIN Verified Successfully!")
                if choose == "ok":
                    account_type2()
            else:
                to_home()
        except:
            to_home()
    button9u = Button(root3,text="Ok",bd='5',height=2,width=20,font="Algerian",fg="black",\
                     bg="dark blue",command=input_value)
    button9u.pack(pady=20,anchor=CENTER,side=RIGHT)
    root3.mainloop()
  
def PinVerification1():
    time.sleep(2)
    root3 = Toplevel()
    obj = ATM()
    root3.geometry("1276x710")
    root3.title("ATM-PIN")
    photo = PhotoImage(file=r"C:\Users\abc\Pictures\Screenshots\Annotation 2023-04-24 152144main.png")
    lab = Label(root3,image=photo)
    lab.place(x=0,y=0) 
    title = Label(root3,text="Please Enter Your CARD Pin !",fg="dark blue",font=("Arial Black",34))
    title.pack(anchor=CENTER,side=TOP)
    button9 = Button(root3,text="Cancel",bd='5',height=2,width=20,font="Algerian",fg="black",\
                     bg="dark blue",command=obj.testing_5)
    button9.pack(pady=20,anchor=CENTER,side=BOTTOM)
    enterpin = Entry(root3,show="*",width=100)
    enterpin.pack(pady=17,anchor=CENTER,side=TOP)
    def account_type1():
        root4 = Toplevel()
        root4.geometry("1276x710")
        root4.title("ATM-Account Type")
        photo = PhotoImage(file=r"C:\Users\abc\Pictures\Screenshots\Annotation 2023-04-24 151733main.png")
        lab = Label(root4,image=photo)
        lab.place(x=0,y=0)
        frame = Frame(root4)
        title = Label(root4,text="Select Transaction Type !",fg="dark blue",font=("Arial Black",34))
        title.pack(anchor=CENTER,side=TOP)
        button1 = Button(frame,text="Current Account",bd='5',height=2,width=20,font="Algerian",fg="black",\
                         bg="dark blue",command=obj.withdraw)
        button2 = Button(frame,text="Saving Account",bd='5',height=2,width=20,font="Algerian",fg="black",\
                         bg="dark blue",command=obj.withdraw)
        button3 = Button(frame,text="Salary Account",bd='5',height=2,width=20,font="Algerian",fg="black",\
                         bg="dark blue",command=obj.withdraw)
        button4 = Button(frame,text="NRI Account",bd='5',height=2,width=20,font="Algerian",fg="black",\
                         bg="dark blue",command=not_release)
        button1.pack(pady=20)
        button2.pack(pady=20)
        button3.pack(pady=20)
        button4.pack(pady=20)
        frame.pack(pady=20,anchor=CENTER,side=RIGHT)
    def input_value():
        try:
            with open("new_pin_code","r") as file:
                pin_value = int(file.readline())
            value = int(enterpin.get())
            if value == pin_value:
                time.sleep(2)
                choose = mb.showinfo("PIN-Vefied","PIN Verified Successfully!")
                if choose == "ok":
                    account_type1()
            else:
                to_home()
        except:
            to_home()
    button9u = Button(root3,text="Ok",bd='5',height=2,width=20,font="Algerian",fg="black",\
                     bg="dark blue",command=input_value)
    button9u.pack(pady=20,anchor=CENTER,side=RIGHT)
    root3.mainloop()

    
def Hindi():
    pass
def English():
    root2 = Toplevel() 
    root2.geometry("1276x710")
    root2.title("ACCOUNT-DEBIT CARD")
    photo = PhotoImage(file=r"C:\Users\abc\Pictures\Screenshots\Annotation 2023-04-24 152334main.png")
    lab = Label(root2,image=photo)
    lab.place(x=0,y=0) 
    title = Label(root2,text="Please Insert Your Card!",fg="dark blue",font=("Arial Black",34))
    title.pack(anchor=CENTER,side=TOP)
    button9 = Button(root2,text="Cancel",bd='5',height=2,width=20,font="Algerian",fg="black",\
                     bg="dark blue",command=testing_5a)
    button9.pack(pady=20,anchor=CENTER,side=BOTTOM)
    def showmessage():
        time.sleep(2)
        clickedok = mb.showinfo("Verified","Your DEBIT Card Details Successfully Verified!")
        if clickedok == "ok":
            TransactionType()
    button = Button(root2,text="Done",bd='5',height=2,width=20,font="Algerian",fg="black",bg="dark blue",command=showmessage)
    button.pack(anchor=CENTER,side=RIGHT)
    root2.mainloop()
def Marathi():
    pass
def Proceed ():
    root1 = Toplevel()
    root1.geometry("1276x710")
    root1.title("ATM-Language")
    photo = PhotoImage(file=r"C:\Users\abc\Pictures\Screenshots\Annotation 2023-04-24 151705main.png")
    lab = Label(root1,image=photo)
    lab.place(x=0,y=0) 
    frame = Frame(root1)
    title = Label(root1,text="Please Select Any One Language To Proceed!...",fg="dark blue",font=("Arial Black",30))
    title.pack(pady=10,anchor=CENTER,side=TOP)
    but1 = Button(frame,text="Hindi",bd='5',height=2,width=20,font="Algerian",fg="black",\
                  bg="dark blue",command=Hindi)
    but2 = Button(frame,text="English",bd='5',height=2,width=20,font="Algerian",fg="black",\
                  bg="dark blue",command=English)
    but3 = Button(frame,text="Marathi",bd='5',height=2,width=20,font="Algerian",fg="black",\
                  bg="dark blue",command=Marathi)
    but1.pack(pady=20)
    but2.pack(pady=20)
    but3.pack(pady=20)
    frame.pack(pady=20,anchor=CENTER,side=RIGHT)
    root1.mainloop()
def for_test():
    obj = ATM()
    if os.path.isfile("avail_balance_money"):
        Proceed()
    else:
        obj.check_locker()
def main():
    root = Toplevel()
    root.geometry("1276x710")
    root.title("ATM")
    photo = PhotoImage(file=r"C:\Users\abc\Pictures\Screenshots\Annotation 2023-04-24 151317main.png")
    lab = Label(root,image=photo)
    lab.place(x=0,y=0)   
    screen1 = Label(root,text= "It Is PRATAP BANKING \nSOLUTIONS",font=("Arial Black",72),fg= "red")
    screen1.pack(anchor=CENTER,side=TOP)
    button = Button(root,text="Cancel!",fg="black",bg="sky blue",bd='5',height=2,width=20,\
                     font="Algerian",command=root.destroy)
    button.pack(pady=20,anchor=CENTER,side=BOTTOM)
    button1 = Button(root,text="Proceed!",fg="black",bg="sky blue",bd='5',height=2,width=20,\
                     font="Algerian",command=for_test)
    button1.pack(pady=20,anchor=CENTER,side=BOTTOM)
    root.mainloop()

root = Tk()
root.geometry("1276x710")
root.title("ATM")
photo = PhotoImage(file=r"C:\Users\abc\Pictures\Screenshots\Annotation 2023-04-24 151532main.png")
lab = Label(root,image=photo)
lab.place(x=0,y=0)
screen1 = Label(root,text= "Welcome!",font=("Arial Black",90),fg= "red")
screen1.pack(anchor=CENTER,side=TOP)
button1 = Button(root,text="Start Banking!",fg="black",bg="sky blue",bd='5',height=4,width=38,\
                     font="Algerian",command=main)
button1.pack(pady=40,anchor=CENTER,side=BOTTOM)
root.mainloop()
