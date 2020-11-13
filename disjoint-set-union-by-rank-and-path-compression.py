from collections import defaultdict
def createGraph():
    g=defaultdict(list)
    return g

def addEdge(g,u,v):
    g[u].append(v)

def find(parent,x):
    if parent[x]==-1:
        return x
    return find(parent,parent[x])

def union(parent,rank,x,y):
    a=find(parent,x)
    b=find(parent,y)
    if rank[a] < rank[b]:
        parent[a] = b
    elif rank[a] > rank[b]:
        parent[b] = a
    else:
        parent[a] = b
        rank[b]+=1

def isCycle(g,n):
    parent=[-1]*n
    rank=[0]*n
    for i in g:
        for j in g[i]:
            x=find(parent,i)
            y=find(parent,j)
            if x==y:
                return True            # THEY BELONG TO SAME SET
            union(parent,rank,x,y)      


if __name__ == "__main__":
    g=createGraph()
    addEdge(g,0,1)
    addEdge(g,1,2)
    addEdge(g,2,3)

    if isCycle(g,4):
        print("YES")
    else:
        print("NO")