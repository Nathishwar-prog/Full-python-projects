def hangman():
    word = "PYTHON"
    guessed = ['_'] * len(word)
    attempts = 6
    
    print("Hangman Game")
    
    while attempts > 0 and '_' in guessed:
        print("\n" + ' '.join(guessed))
        print(f"Attempts left: {attempts}")
        guess = input("Guess a letter: ").upper()
        
        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed[i] = guess
        else:
            attempts -= 1
            print("Wrong guess!")
    
    if '_' not in guessed:
        print(f"\nCongratulations! The word was {word}")
    else:
        print(f"\nGame over! The word was {word}")

hangman()
