import random

number=['0','1','2','3','4','5','6','7','8','9']
letter=('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')    
char=['!','@','#','$','%','&','^','*','-','_','?','<','>','~','/']

num_number=int(input("Numers:"))
num_letter=int(input("Alphabets:"))
num_charecter=int(input("Charecters:"))

password=[]

password+=random.choices(number,k=num_number)
password+=random.choices(letter,k=num_letter)
password+=random.choices(char,k=num_charecter)

random.shuffle(password)
final_password=''.join(password)

print("Generated Password: ",final_password)

length=len(final_password)
if(length>=16):
    print("Very strong Pasword")
elif(length<=15 and length>=10):
    print("Strong Password")
elif(length<=9 and length>=6):
    print("Moderate Password")
else:
    print("Weak Password")

