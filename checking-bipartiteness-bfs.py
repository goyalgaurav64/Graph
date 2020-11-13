from collections import defaultdict
def createGraph():
    return defaultdict(list)

def addEdge(g,u,v):
    g[u].append(v)
    g[v].append(u)

def isBigraphUtil(g,color,v,vis):
    q=[]
    q.append(v)
    color[v]=0
    vis[v]=True
    while(q):
        cur=q.pop(0)
        for i in g[cur]:
            if color[i]==color[cur]:
                return False
            if color[i]==-1:
                color[i]=1-color[cur]
                q.append(i)
    return True



def isBiGraph(g,n):
    color=[-1]*(n+1)
    vis=[False]*(n+1)
    for i in range(1,n+1):
        if color[i]==-1:
            if not isBigraphUtil(g,color,i,vis):
                return False
    return True

if __name__ == "__main__":
    g=createGraph()
    n=5
    addEdge(g, 1, 2) 
    # addEdge(g, 2, 3) 
    addEdge(g, 3, 4) 
    addEdge(g, 4, 5) 
    addEdge(g, 3, 5) 
    # addEdge(g, 6, 1)
    if isBiGraph(g,n):
        print("Yes it is a bigraph")
    else:
        print("Not a bigraph")