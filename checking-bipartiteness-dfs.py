from collections import defaultdict
def createGraph():
    return defaultdict(list)

def addEdge(g,u,v):
    g[u].append(v)
    g[v].append(u)

def isBiGraph(g,v,vis,color):
    vis[v]=True
    for i in g[v]:
        if vis[i]==False:
            vis[i]=True
            color[i]=1-color[v]
            if isBiGraph(g,i,vis,color) is False:
                return False
        elif color[i]==color[v]:
            return False
    return True

if __name__ == "__main__":
    g=createGraph()
    n=6
    addEdge(g, 1, 2) 
    addEdge(g, 2, 3) 
    addEdge(g, 3, 4) 
    addEdge(g, 4, 5) 
    addEdge(g, 5, 6) 
    addEdge(g, 6, 1)
    visited=[False]*(n+1)
    color=[0]*(n+1)
    if isBiGraph(g,1,visited,color):
        print("Yes it is a bigraph")
    else:
        print("Not a bigraph")