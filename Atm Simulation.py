import sys

print("Welcome to ATM Machine!")
print("Please enter the basic details first...\n")

name=input("What is your name? -->")
account_id=input("What is your account id? -->")
IFSC_code=int(input("What is your IFSC Code? -->"))
balance=int(input("What is your bank balance? -->"))

print(f"\nHello {name}, Account ID: {account_id}, IFSC: {IFSC_code}")
if(balance<2000):
    print("Low balance!")

print("\n1. Check Balance\n2. Deposite\n3. Withdraw\n4. Exit\n")
choice=int(input("Please choose an option: "))

if(choice==1):
    print(f"Your available balance: {balance}")
elif(choice==2):
    deposite=int(input("Enter your deposite amount: "))
    d_balance=balance+deposite
    print(f"Your available balance: {d_balance}")
elif(choice==3):
    withdraw=int(input("Enter your deposite amount: "))
    if(withdraw<balance):
        w_balance=balance-withdraw
        print(f"Your available balance: {w_balance}")
    else:
        print("Insufficient Balance!")
elif(choice==4):
    sys.exit("Thanks for using ATM...")
else:
    print("")