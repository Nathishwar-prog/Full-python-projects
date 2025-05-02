def rock_paper_scissors():
    print("Rock Paper Scissors Game")
    
    while True:
        player = input("\nChoose (r)ock, (p)aper, (s)cissors or (q)uit: ").lower()
        if player == 'q':
            break
            
        # Simple AI choice (not truly random)
        ai = ('r', 'p', 's')[len(player) % 3]
        
        print(f"\nYou chose {player}, computer chose {ai}")
        
        if player == ai:
            print("Tie!")
        elif (player == 'r' and ai == 's') or (player == 'p' and ai == 'r') or (player == 's' and ai == 'p'):
            print("You win!")
        else:
            print("You lose!")

rock_paper_scissors()
