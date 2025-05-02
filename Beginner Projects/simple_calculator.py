def simple_calculator():
    print("Simple Calculator")
    print("Operations available:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")
    
    while True:
        # Get user input
        operation = input("Enter operation (1-5 or +-*/): ")
        
        # Exit condition
        if operation == '5' or operation.lower() == 'exit':
            print("Goodbye!")
            break
        
        # Validate operation
        if operation not in ['1', '2', '3', '4', '+', '-', '*', '/']:
            print("Invalid operation. Please try again.")
            continue
        
        # Get numbers
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid number. Please enter numeric values.")
            continue
        
        # Perform calculation
        if operation == '1' or operation == '+':
            result = num1 + num2
            print(f"Result: {num1} + {num2} = {result}")
        elif operation == '2' or operation == '-':
            result = num1 - num2
            print(f"Result: {num1} - {num2} = {result}")
        elif operation == '3' or operation == '*':
            result = num1 * num2
            print(f"Result: {num1} * {num2} = {result}")
        elif operation == '4' or operation == '/':
            if num2 == 0:
                print("Error: Cannot divide by zero!")
            else:
                result = num1 / num2
                print(f"Result: {num1} / {num2} = {result}")
        
        print()  # Add empty line for better readability

# Start the calculator
simple_calculator()
