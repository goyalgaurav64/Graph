from collections  import defaultdict
def createGraph():
    return defaultdict(list)

def addEdge(g,u,v):
    g[u].append(v)
    g[v].append(u)

def dfs(g,u,disc,low,parent,time):
    disc[u]=low[u]=time
    for v in g[u]:
        if disc[v] is -1:
            parent[v] = u
            dfs(g,v,disc,low,parent,time+1)
            low[u] = min(low[u] , low[v])

            if low[v] > disc[u]:
                print("%d %d"%(u,v))
        
        elif v is not parent[u]:
            low[u] = min(low[u] , disc[v])

def BridgesByTarjan(g,n):
    disc=[-1]*n
    low=[-1]*n
    parent=[-1]*n
    for i in range(n):
        if disc[i] is -1:
            dfs(g,i,disc,low,parent,0)



if __name__ == "__main__":
    g1=createGraph()
    print("Bridges in Graph:")
    addEdge(g1,0,1)
    addEdge(g1,1,2)
    addEdge(g1,0,2)
    addEdge(g1,0,3)
    addEdge(g1,3,4)

    BridgesByTarjan(g1,5)
    print("Bridges in Graph:")

    g2=createGraph()
    addEdge(g2,0,1)
    addEdge(g2,0,2)
    addEdge(g2,1,2)
    addEdge(g2,1,3)
    addEdge(g2,1,4)
    addEdge(g2,1,6)
    addEdge(g2,3,5)
    addEdge(g2,4,5)
    BridgesByTarjan(g2,7)
    print("Bridges in Graph:")

    g3=createGraph()
    addEdge(g3,0,1)
    addEdge(g3,1,2)
    addEdge(g3,2,3)
    BridgesByTarjan(g3,4)