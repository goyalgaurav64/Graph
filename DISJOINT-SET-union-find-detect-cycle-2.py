from collections import defaultdict
def createGraph():
    return defaultdict(list)

def addEdge(g,u,v):
    g[u].append(v)
    # g[v].append(u)


def find_root(parent,x):
    if parent[x]==-1:
        return x
    return find_root(parent,parent[x])

def union(parent,x,y):
    a=find_root(parent,x)
    b=find_root(parent,y)
    parent[a]=b

def hasCycleUtil(g,parent,cur):
    for i in g[cur]:
        x=find_root(parent,cur)
        y=find_root(parent,i)
        if x==y:
            return True
        union(parent,x,y)
    return False

def hasCycle(g,n):
    parent=[-1]*n
    for i in g:
        if hasCycleUtil(g,parent,i) is True:
            return True
    return False
if __name__ == "__main__":
    n=3
    g=createGraph()
    addEdge(g,0,1)
    addEdge(g,1,2)
    addEdge(g,0,2)

    if hasCycle(g,n):
        print("HAS CYCLE")
    else:
        print("NOT")