def showboard(spots):
    board = (f"|{spots[1]}|{spots[2]}|{spots[3]}| \n"
             f"|{spots[4]}|{spots[5]}|{spots[6]}| \n"
             f"|{spots[7]}|{spots[8]}|{spots[9]}|")
    print(board)

def check_turn(turn):
    if turn % 2 == 0:
        return 'O'
    else:
        return 'X'

def win(spots):
    for i in range(1, 8, 3):
        if spots[i] == spots[i + 1] == spots[i + 2]:
            return True
    for i in range(1, 4):
        if spots[i] == spots[i + 3] == spots[i + 6]:
            return True
    if spots[1] == spots[5] == spots[9] or spots[3] == spots[5] == spots[7]:
        return True
    return False