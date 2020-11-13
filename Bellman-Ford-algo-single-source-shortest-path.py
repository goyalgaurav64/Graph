import sys
def createGraph(g,u,v,cost):
    g.append([u,v,cost])

def printRoutes(p,d,n):
    print("EDGES \t DISTANCE FROM  SOURCE")
    for i in range(n):
        if p[i] is not -1:
            print(p[i],"---->",i,"\t",d[i])

def BellmanFord(g,src,n):
    parent=[None]*n
    dist=[sys.maxsize]*n
    dist[src]=0
    parent[src]=-1
    i,j=0,0
    for i in range(n-1):
        for u,v,w in g:
            if dist[u] is not sys.maxsize and dist[v] > dist[u] + w:
                parent[v]=u
                dist[v] = dist[u] + w
    for u,v,w in g:
        if dist[u] is not sys.maxsize and dist[v] > dist[u] + w:
            print("Graph contains negative edge weight cycle")
            return
    printRoutes(parent,dist,n)


if __name__ == "__main__":
    g=[]
    createGraph(g,0,1,-1)
    createGraph(g,0,2,4)
    createGraph(g,1,2,3)
    createGraph(g,1,3,2)
    createGraph(g,1,4,2)
    createGraph(g,3,2,5)
    createGraph(g,3,1,1)
    createGraph(g,4,3,-3)

    BellmanFord(g,4,5)