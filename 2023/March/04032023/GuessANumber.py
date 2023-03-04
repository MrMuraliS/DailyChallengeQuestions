import random

user_input = int(input("Enter a number between 1 - 10: "))
sys_input = random.randint(1, 10)

while True:
    print(f"{user_input=}, {sys_input=}")
    if user_input != sys_input:
        print("System WON the game. Keep trying...")
        user_input = int(input("Enter a number between 1 - 10 again: "))
        sys_input = random.randint(1, 10)
    else:
        print("Congrats, You won the game..")
        print("Do you need to continue ? select following options: \n 1- Yes\n 2- No")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            user_input = int(input("Enter a number between 1 - 10 again: "))
            sys_input = random.randint(1, 10)
        elif choice == 2:
            print("Thanks for playing, Bye for now.. ")
            break
        else:
            print("You have entered wrong number, closing the game..!")
            break
