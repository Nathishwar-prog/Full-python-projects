def temp_converter():
    print("Temperature Converter")
    
    while True:
        print("\nOptions:")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Exit")
        
        choice = input("Choose (1-3): ")
        
        if choice == "1":
            c = float(input("Enter Celsius: "))
            f = (c * 9/5) + 32
            print(f"{c}°C = {f:.1f}°F")
        elif choice == "2":
            f = float(input("Enter Fahrenheit: "))
            c = (f - 32) * 5/9
            print(f"{f}°F = {c:.1f}°C")
        elif choice == "3":
            break
        else:
            print("Invalid choice")

temp_converter()
