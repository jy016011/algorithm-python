from random import randint
print("Welcome to python casino.")
#pc_choice = 50
pc_choice = randint(1,100)
Life = 8
while Life > 0:
    user_choice = int(input("Choose number 1 to 100: "))
    if user_choice == pc_choice:
        print("Congraturations! You are correct!")
        break
    elif user_choice > pc_choice:
        Life -= 1
        print(f"Lower! You have {Life} chances")
    else:
        Life -= 1
        print(f"Higher! You have {Life} chances")

if Life == 0:
    print("You lose play again if you wanna win.")

