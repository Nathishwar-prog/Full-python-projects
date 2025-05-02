def dice_roller():
    import time
    
    print("Dice Rolling Simulator")
    
    while True:
        input("\nPress Enter to roll (q to quit)...")
        if input() == 'q':
            break
            
        # Simple pseudo-random using time
        roll = int(time.time() * 1000) % 6 + 1
        print(f"You rolled: {roll}")

dice_roller()
