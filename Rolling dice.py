import random as r

num=int(input("Enter how many dices you wanna roll: "))
count=0

while True:
    choice=input("Type(y/n): ").lower()
    if choice =="y":
        for i in range (1,num+1):
            dice=r.randint(1,6)
            print(f"{dice}",end=" ")

        count+=1
        print()
        print(f"Total dice roling count:{count} times...")

    elif choice=="n":
            print("Thanks for playing...")
            break
    
    else:
            print("Invalid input...")





