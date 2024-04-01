from show import showboard,check_turn,win
import os 
spots = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}

playing = True
turn = 0
prev = -1
complete = False
while playing:
    os.system('cls' if os.name == 'nt' else 'clear')
    showboard(spots)
    if prev == turn:
        print("Invalid move")
    prev = turn
    print("Player " + str((turn % 2) + 1) + "'s turn:pick your spot or press 'q' to quit.")
    choice = input("Enter a spot: ")
    if choice == 'q':
        playing = False
    elif type(choice) != int and int(choice) in spots:
        if  not spots[int(choice)] in {'X','O'}:
        
            turn += 1
            spots[int(choice)] = check_turn(turn)
    if win(spots):playing,complete = False,True
    if turn == 9:playing = False

os.system('cls' if os.name == 'nt' else 'clear')
showboard(spots)
if complete:
    print("Player " + str((turn % 2) + 1) + " wins!")
else:
    print("It's a tie!")    

print("Thanks for playing!")
        