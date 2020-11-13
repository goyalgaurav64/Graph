def isValid(maze,i,j,m,n,vis):
    return i >= 0 and j >= 0 and i < m and j < n and maze[i][j] is 1 and vis[i][j] is False

def dfs(maze,i,j,x,y,m,n,vis):
    inv=1000000
    if not isValid(maze,i,j,m,n,vis):
        return inv
    if i is x and  j is y:
        return 0
    vis[i][j] = True
    
    bottom=dfs(maze,i+1,j,x,y,m,n,vis)+1
    right=dfs(maze,i,j+1,x,y,m,n,vis)+1
    top=dfs(maze,i-1,j,x,y,m,n,vis)+1
    left=dfs(maze,i,j-1,x,y,m,n,vis)+1


    vis[i][j]=False
    return min(bottom,right,left,top)


def findSoln(maze):
    m=len(maze)
    n=len(maze[0])
    vis=[[False for i in range(n)]for j in range(m)]

    ans=dfs(maze,0,0,0,9,m,n,vis)
    return ans


if __name__ == "__main__":
    # maze = [[1, 0, 0, 0], 
    #         [1, 1, 0, 1], 
    #         [0, 1, 0, 0], 
    #         [1, 1, 1, 1]]
    maze=[
		[1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
		[0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
		[0, 0, 1, 0, 1, 1, 1, 0, 0, 1],
		[1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
		[0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
		[1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
		[0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
		[0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
		[1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
		[0, 0, 1, 0, 0, 1, 1, 0, 0, 1]
	]
    ans=findSoln(maze)
    if ans > 1000000:
        print("No path Possible")
    else:
        print(ans)