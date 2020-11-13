import sys
def printSPG(d,n):
    print("SOURCE \t DISTANCE FROM SOURCE")
    for i in range(n):
        print(i,"\t\t",d[i])


def FindminVertex(dist,vis,n):
    min=sys.maxsize
    vertex=-1
    for i in range(n):
        if vis[i] is False and min > dist[i]:
            min = dist[i]
            vertex=i
    return vertex

def spgDij(g,n,src):
    parent=[None]*n
    vis=[False]*n
    dist=[sys.maxsize]*n
    dist[src]=0
    for i in range(n):
        u=FindminVertex(dist,vis,n)
        vis[u]=True
        for v in range(n):
            if g[u][v] > 0 and vis[v] is False and dist[v] > dist[u] + g[u][v] and dist[u] is not sys.maxsize:
                dist[v] = g[u][v] + dist[u]
    printSPG(dist,n)





if __name__ == "__main__":
    # g=[[0, 4, 0, 0, 0, 0, 0, 8, 0], 
    #     [4, 0, 8, 0, 0, 0, 0, 11, 0], 
    #     [0, 8, 0, 7, 0, 4, 0, 0, 2], 
    #     [0, 0, 7, 0, 9, 14, 0, 0, 0], 
    #     [0, 0, 0, 9, 0, 10, 0, 0, 0], 
    #     [0, 0, 4, 14, 10, 0, 2, 0, 0], 
    #     [0, 0, 0, 0, 0, 2, 0, 1, 6], 
    #     [8, 11, 0, 0, 0, 0, 1, 0, 7], 
    #     [0, 0, 2, 0, 0, 0, 6, 7, 0] 
    #     ];
    g=[[0,1,4,0,0,0],
       [1,0,4,2,7,0],
       [4,4,0,3,5,0],
       [0,2,3,0,4,6],
       [0,7,5,4,0,7],
       [0,0,0,6,7,0]]
    spgDij(g,6,2) 