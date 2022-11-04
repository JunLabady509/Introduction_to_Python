from playing import startGame

def print_menu():
    print("_______________________________________________")
    print("Select an Option:")
    print("1. New Game")
    print("2. Load Saved Game")
    print("3. About")
    print("4. Exit")
    print("_______________________________________________")

while True:
    print_menu()
    choice = int(input("Please make a choice >> "))

    if choice == 1:
        startGame()

    elif choice == 2:
        print("Choose your saved game >> ")

    elif choice == 3:
        print("Loading about...")

    elif choice == 4:
        print("Exiting...")

    else:
        print("Invalid option, please try again")

