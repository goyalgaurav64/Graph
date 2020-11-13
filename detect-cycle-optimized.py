from collections import defaultdict
def createGraph():
    return defaultdict(list)

def addEdge(g,u,v):
    g[u].append(v)

def isCyclic(g,vis,cur):
    vis[cur]=1
    for i in g[cur]:
        if vis[i]==1:
            return True
        if vis[i]==0 and isCyclic(g,vis,i)==True:
            return True
    vis[cur]=2
    return False

def detectCycle(g,n):
    visited=[0]*n
    for i in range(n):
        if visited[i]==0:
            if(isCyclic(g,visited,i)==True):
                return True
    return False 



if __name__ == "__main__":
    g=createGraph()
    addEdge(g,0,1)
    addEdge(g,1,2)
    addEdge(g,2,3)
    addEdge(g,3,4)
    addEdge(g,4,5)

    if detectCycle(g,6) is True:
        print("Has cycle")
    else:
        print("Not having cycle")