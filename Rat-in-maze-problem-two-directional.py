def isValid(maze,x,y,m,n):
    if x >= 0 and y >= 0 and x < m and y < n and maze[x][y] is 1:
        return True
    return False

def dfs(maze,sol,x,y):
    m,n=len(maze),len(maze[0])
    if x is m-1 and  y is n-1 and maze[x][y] is 1:
        sol[x][y]=1
        return True
    if  isValid(maze,x,y,m,n) is True:
        sol[x][y] = 1
    # vis[i][j] = True
    
        if dfs(maze,sol,x+1,y) is True:
            return True
        if dfs(maze,sol,x,y+1) is True:
            return True
        sol[x][y]=0
        return False

    # vis[i][j]=False

def printSol(sol,m,n):
    for i in range(m):
        for j in range(n):
            print(sol[i][j],end=" ")
        print()

def findSoln(maze):
    m=len(maze)
    n=len(maze[0])
    # vis=[[False for i in range(n)]for j in range(m)]
    sol=[[0 for i in range(n)]for j in range(m)]

    dfs(maze,sol,0,0)

    printSol(sol,m,n)



if __name__ == "__main__":
    maze = [[1, 0, 0, 0], 
            [1, 1, 0, 1], 
            [0, 1, 0, 0], 
            [1, 1, 1, 1]]
    # maze=[
	# 	[1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
	# 	[0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
	# 	[0, 0, 1, 0, 1, 1, 1, 0, 0, 1],
	# 	[1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
	# 	[0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
	# 	[1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
	# 	[0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
	# 	[0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
	# 	[1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
	# 	[0, 0, 1, 0, 0, 1, 1, 0, 0, 1]
	# ]
    ans=findSoln(maze)
    if ans is False:
        print("Solution is not possible")