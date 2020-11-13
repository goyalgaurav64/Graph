def dfs(screen,newC,prevC,x,y):
    m=len(screen)
    n=len(screen[0])
    if x < 0 or x >= m or y < 0 or y >= n or screen[x][y] is not prevC or screen[x][y] is newC:
        return
    screen[x][y] = newC
    dfs(screen,newC,prevC,x+1,y) 
    dfs(screen,newC,prevC,x,y+1) 
    dfs(screen,newC,prevC,x-1,y) 
    dfs(screen,newC,prevC,x,y-1)

def printScreen(screen,m,n):
    for i in range(m):
        for j in range(n):
            print(screen[i][j],end=" ")
        print()
     


def floodFill(screen,newC,x,y):
    m=len(screen)
    n=len(screen[0])
    prevC=screen[x][y]
    dfs(screen,newC,prevC,x,y)

    printScreen(screen,m,n)




if __name__ == "__main__":
    screen=[[1, 1, 1, 1, 1, 1, 1, 1], 
          [1, 1, 1, 1, 1, 1, 0, 0], 
          [1, 0, 0, 1, 1, 0, 1, 1], 
          [1, 2, 2, 2, 2, 0, 1, 0], 
          [1, 1, 1, 2, 2, 0, 1, 0], 
          [1, 1, 1, 2, 2, 2, 2, 0], 
          [1, 1, 1, 1, 1, 2, 1, 1], 
          [1, 1, 1, 1, 1, 2, 2, 1]]
    newColor=3
    print("Updated screen is:")
    floodFill(screen,newColor,4,4)