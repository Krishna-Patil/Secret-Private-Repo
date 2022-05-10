from typing import List


boardcount = 0


def isboardok(chessboard: List, row: int, col: int):
    for c in range(col):
        if(chessboard[row][c] == 'Q'):
            return False
    for r, c in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if(chessboard[r][c] == 'Q'):
            return False
    for r, c in zip(range(row+1, len(chessboard), 1), range(col-1, -1, -1)):
        if(chessboard[r][c] == 'Q'):
            return False
    return True


def displayboard(chessboard: List):
    for row in chessboard:
        print(row)
    print()


def placenqueens(chessboard: List, col: int):
    global boardcount
    if(col >= len(chessboard)):
        boardcount += 1
        print("Board"+str(boardcount))
        print("======================")
        displayboard(chessboard)
        print("======================\n\n")
    else:
        for row in range(len(chessboard)):
            chessboard[row][col]='Q'
            if(isboardok(chessboard,row,col)==True):
                placenqueens(chessboard,col+1)
            chessboard[row][col]='.'


chessboard=[]
N=int(input("Enter chessboard size: "))
for i in range(N):
 row=["."]*N
 chessboard.append(row)
placenqueens(chessboard,0)
