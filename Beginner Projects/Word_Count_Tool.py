def word_counter():
    print("Word Count Tool")
    text = input("Enter your text: ")
    
    words = text.split()
    char_count = len(text)
    word_count = len(words)
    
    print(f"\nCharacters: {char_count}")
    print(f"Words: {word_count}")

word_counter()
