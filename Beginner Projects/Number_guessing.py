def number_guessing_game():
    print("Number Guessing Game")
    print("I'm thinking of a number between 1 and 100. Can you guess it?")
    
    # Generate a random number without using random library
    # Using system time for simple pseudo-randomness
    import time
    target = int(time.time() * 1000) % 100 + 1
    
    attempts = 0
    max_attempts = 10
    
    while attempts < max_attempts:
        attempts += 1
        try:
            guess = int(input(f"Attempt {attempts}/{max_attempts}. Your guess: "))
        except ValueError:
            print("Please enter a valid number between 1 and 100.")
            continue
            
        if guess < 1 or guess > 100:
            print("Your guess must be between 1 and 100!")
            continue
            
        if guess == target:
            print(f"Congratulations! You guessed the number in {attempts} attempts!")
            return
        elif guess < target:
            print("Too low! Try a higher number.")
        else:
            print("Too high! Try a lower number.")
    
    print(f"Game over! The number was {target}. Better luck next time!")

# Start the game
number_guessing_game()
