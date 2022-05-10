def printSolution(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()


def isSafe(row, col, nd, rd, rowLookup, ndLookup, rdLookup):
    if (ndLookup[nd[row][col]] or rdLookup[rd[row][col]] or rowLookup[row]):
        return False
    return True


def solveNQueensUtil(board, col, nd, rd, rowLookup, ndLookup, rdLookup):
    if(col >= N):
        return True
    for i in range(N):
        if(isSafe(i, col, nd, rd, rowLookup, ndLookup, rdLookup)):
            board[i][col] = 1
            rowLookup[i] = True
            ndLookup[nd[i][col]] = True
            rdLookup[rd[i][col]] = True
            if(solveNQueensUtil(board, col + 1, nd, rd, rowLookup, ndLookup, rdLookup)):
                return True
            board[i][col] = 0
            rowLookup[i] = False
            ndLookup[nd[i][col]] = False
            rdLookup[rd[i][col]] = False
    return False


def solveNQueens(N):
    board = [[0 for i in range(N)] for j in range(N)]
    nd = [[0 for i in range(N)] for j in range(N)]
    rd = [[0 for i in range(N)] for j in range(N)]
    rowLookup = [False] * N
    x = 2 * N - 1
    ndLookup = [False] * x
    rdLookup= [False] * x
    for r in range(N):
        for c in range(N):
            nd[r][c] = r + c
            rd[r][c] = r - c + N - 1

    if(solveNQueensUtil(board, 0, nd, rd,rowLookup, ndLookup,rdLookup) == False):
        print("Solution does not exist")
        return False
    printSolution(board)
    return True

N=int(input("Enter a Number: "))
solveNQueens(N)