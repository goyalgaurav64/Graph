def printSudoku(grid):
    m,n=len(grid),len(grid[0])
    for i in range(m):
        for j in range(n):
            print(grid[i][j],end=" ")
        print()

def isValid(board,x,y,num):
    for i in range(len(board[0])):
        if board[x][i] is num:
            return False
    
    for i in range(len(board)):
        if board[i][y] is num:
            return False
    
    a = x//3 * 3
    b = y//3 * 3
    for i in range(a,a+3):
        for j in range(b,b+3):
            if board[i][j] is num:
                return False
    return True

def solveSudoku(board,i,j):
    m=len(board)
    n=len(board[0])
    if i is m:
        printSudoku(board)
        return True
    ni,nj=-1,-1
    if j is n-1:
        ni,nj=i+1,0
    else:
        ni,nj=i,j+1
    if board[i][j] is not 0:
        solveSudoku(board,ni,nj)
    else:
        for num in range(1,10):
            if isValid(board,i,j,num) is True:
                board[i][j] = num
                solveSudoku(board,ni,nj)
                board[i][j] = 0


if __name__ == "__main__":
    grid=[[3, 0, 6, 5, 0, 8, 4, 0, 0 ],
          [5, 2, 0, 0, 0, 0, 0, 0, 0],
          [0, 8, 7, 0, 0, 0, 0, 3, 1],
          [0, 0, 3, 0, 1, 0, 0, 8, 0],
          [9, 0, 0, 8, 6, 3, 0, 0, 5],
          [0, 5, 0, 0, 9, 0, 6, 0, 0],
          [1, 3, 0, 0, 0, 0, 2, 5, 0],
          [0, 0, 0, 0, 0, 0, 0, 7, 4],
          [0, 0, 5, 2, 0, 6, 3, 0, 0]]
    ans=solveSudoku(grid,0,0)
    if ans is False:
        print("Solution is not possible")