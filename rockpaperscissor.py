times=int(input("Enter the number of times you wanna play:"))
import random as r

emoji={"r":"✊", "p":"✋", "s":"✌️"}
rpc=("r", "p", "s")
win=0
lose=0
play=0

while play<times: 
    user=input("Enter your choice: ")
    if user not in rpc:
        print("Invalid choice...")
        continue

    bot=r.choice(rpc)
    print(f"You:{emoji[user]} | Bot:{emoji[bot]}")

    if ((user=="r" and bot=="p") or
        (user=="p" and bot=="s") or 
        (user=="s" and bot=="r")):
        print("You lose.")
        lose+=1
    elif (user==bot):
        print("It's draw.")
    else: 
        print("You win.")
        win+=1
    play+=1

print()
print("\nGame Over!")
print(f"Your Score: {win}; Bot's Score: {lose}")
if (win>lose):
    print("🎉 You are the winner!")
elif  win == lose:
    print("It's a tie!")
else:
    print("🤖 Bot is the winner.")