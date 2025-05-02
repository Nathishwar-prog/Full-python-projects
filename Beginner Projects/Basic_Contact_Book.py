def contact_book():
    contacts = {}
    
    while True:
        print("\nContact Book:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Exit")
        
        choice = input("Choose option (1-3): ")
        
        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            contacts[name] = phone
            print("Contact added!")
        elif choice == "2":
            print("\nContacts:")
            for name, phone in contacts.items():
                print(f"{name}: {phone}")
        elif choice == "3":
            break
        else:
            print("Invalid choice")

contact_book()
