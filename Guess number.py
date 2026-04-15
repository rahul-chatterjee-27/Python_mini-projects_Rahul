import random as r

print("You have to enter lower and upper limits and guess the numbers in between. You have 10 limited moves.")

num1=int(input("Enter the lower limit: "))
num2=int(input("Enter the upper limit: "))
num=r.randint(num1,num2)

count=1
while count<=10:
    guess=int(input(f"Guess number in between {num1}-{num2}: "))
    if guess<num:
        print("Noooo! Try high number...!")
        count+=1
    elif guess>num:
        print("Noooo! Try low number...!")
        count+=1
    else:
        left=10-count
        score=left*25.25
        print(f"YAH! You got the number...It's {num}")
        print(f"Your left moves: {left} and your score is {score}")
        break
    if count==10:
            print(f"Sorry... You are out of move. Well, the number was {num}") 
            break