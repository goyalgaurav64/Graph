def floydWarshall(g,n):
    dist=[[None for i in range(n)]for j in range(n)]
    for i in range(n):
        for j in range(n):
            dist[i][j]=g[i][j]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] is float('inf') or dist[k][j] is float('inf'):
                    continue
                else:
                    dist[i][j]=min(dist[i][j] , dist[i][k] + dist[k][j])
    
    for i in range(n):
        if dist[i][i] < 0:
            print("Graph contains negative edge weight cycles")
            return
    
    print("SOURCE DESTINATION \t DISTANCE IS")
    for i in range(n):
        for j in range(n):
            print(i,"to",j,"\t",dist[i][j])
        print()

if __name__ == "__main__":
    i=float('inf')
    g = [[0,5,i,10], 
        [i,0,3,i], 
        [i, i, 0,1], 
        [i, i, i, 0]]
    floydWarshall(g,4)