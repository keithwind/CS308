N = 8
ld = [0] * 30
rd = [0] * 30
 

cl = [0] * 30
 
def printSolution(board):
    for i in range(N):
        for j in range(N):
            print(" Q " if board[i][j] == 1 else " . ", end="")
        print()
 
 
def solveNQUtil(board, col):
    if col >= N:
        return True
    for i in range(N):

        if (ld[i - col + N - 1] != 1 and rd[i + col] != 1) and cl[i] != 1:
            # Place this queen in board[i][col]
            board[i][col] = 1
            ld[i - col + N - 1] = rd[i + col] = cl[i] = 1
 
            # Recur to place the rest of the queens
            if solveNQUtil(board, col + 1):
                return True
 
            board[i][col] = 0  # BACKTRACK
            ld[i - col + N - 1] = rd[i + col] = cl[i] = 0
 

    return False
 
 
def solveNQ():
    board = [[0 for _ in range(N)] for _ in range(N)]
 
    if not solveNQUtil(board, 0):
        print("Solution does not exist")
        return False
 
    printSolution(board)
    return True
 

if __name__ == "__main__":
    solveNQ()