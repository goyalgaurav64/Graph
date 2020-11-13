from collections import defaultdict
def createGraph():
    return defaultdict(list)

def addEdge(g,u,v):
    g[u].append(v)
    g[v].append(u)


def dfs(g,u,time,disc,low,ap,parent):
    c=0  # It keeps track of childrens
    disc[u]=low[u]=time
    for v in g[u]:
        if disc[v] is -1:
            c += 1
            parent[v] = u
            dfs(g,v,time+1,disc,low,ap,parent)
            low[u] = min(low[u] , low[v])
            if parent[u] is -1 and c > 1:
                ap[u] = True
            if parent[u] is not -1 and low[v] >= disc[u]:
                ap[u] = True
        elif v is not parent[u]:
            low[u] = min(low[u] , disc[v])
    
def APbyTarjans(g,n):
    ap=[False]*n    # ARTICULATION POINTS ARRAY
    low=[-1]*n
    disc=[-1]*n
    parent=[-1]*n
    for i in range(n):
        if disc[i] is -1:
            dfs(g,i,0,disc,low,ap,parent)
    
    print("Articulation Points Are:")
    for i in range(n):
        if ap[i] is True:
            print(i,end=' ')


if __name__ == "__main__":
    g1=createGraph()
    addEdge(g1,0,1)
    addEdge(g1,0,2)
    addEdge(g1,0,3)
    addEdge(g1,3,4)
    addEdge(g1,3,5)

    APbyTarjans(g1,6)
    print()
    g2=createGraph()
    addEdge(g2,0,1)
    addEdge(g2,0,2)
    addEdge(g2,1,3)
    addEdge(g2,2,3)
    addEdge(g2,2,5)
    addEdge(g2,3,4)
    addEdge(g2,5,6)

    APbyTarjans(g2,7)