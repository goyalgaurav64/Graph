def isSafe(g,u,color,c,n):
    for i in range(n):
        if g[u][i] is 1 and color[i] is c:
            return False
    return True

def graphColoringUtil(g,color,m,n,u):
    if u is n:
        return True
    for i in range(1,m+1):
        if isSafe(g,u,color,i,n):
            color[u]=i
            if graphColoringUtil(g,color,m,n,u+1):
                return True
        color[u]=0

def graphColoring(g,m,n):
    color=[0]*n
    if not graphColoringUtil(g,color,m,n,0):
        return False
    printSolution(color)

def printSolution(color):
    print("Graph coloring can be:")
    for i in color:
        print(i,end=" ")



if __name__ == "__main__":
    g=[[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]]
    if graphColoring(g,3,4) is False:
        print("Graph coloring is not possible")