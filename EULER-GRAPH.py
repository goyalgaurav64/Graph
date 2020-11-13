from collections import defaultdict
def createGraph():
    return defaultdict(list)

def addEdge(g,u,v):
    g[u].append(v)
    g[v].append(u)

def dfs(g,cur,n,vis):
    vis[cur]=True
    for i in g[cur]:
        if vis[i] is False:
            dfs(g,i,n,vis)

def isConnected(g,n):
    vis=[False]*n
    node=-1
    for i in range(n):
        if len(g[i]) > 0:
            node=i
            break
    if node==-1:
        return True

    dfs(g,node,n,vis)
    
    for i in range(n):
        if vis[i] is False and len(g[i]) > 0:
            return False
    return True


def isEuler(g,n):
    if not isConnected(g,n):
        return 0
    odd=0
    for i in range(n):
        if len(g[i]) % 2 is not 0:
            odd+=1
    if odd > 2:
        return 0
    elif odd == 2:
        return 1
    else:
        return 2


if __name__ == "__main__":
    g=createGraph()
    addEdge(g,0,1)
    addEdge(g,0,2)
    addEdge(g,1,2)
    addEdge(g,2,3)
    addEdge(g,2,4)
    addEdge(g,3,4)

    ans=isEuler(g,5)
    if ans is 0:
        print("Not an Euler Graph")
    elif ans is 1:
        print("Semi Eulerian Graph")
    else:
        print("Eulerian Graph")