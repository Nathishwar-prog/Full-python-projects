def adventure_game():
    print("~ The Mysterious Forest ~")
    print("You find yourself at the edge of a dark forest.")
    
    while True:
        print("\nOptions:")
        print("1. Enter the forest")
        print("2. Walk around the perimeter")
        print("3. Go home")
        
        choice = input("What will you do? (1-3): ")
        
        if choice == "1":
            print("\nYou venture into the forest and find a hidden treasure!")
            break
        elif choice == "2":
            print("\nYou encounter a friendly squirrel who gives you directions.")
        elif choice == "3":
            print("\nYou return home safely.")
            break
        else:
            print("\nInvalid choice. Try again.")

adventure_game()
