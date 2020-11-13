def addEdge(g,u,v,cost):
    g.append([u,v,cost])


def find(parent,x):
    if parent[x]==-1:
        return x
    return find(parent,parent[x])

def union(parent,rank,x,y):
    a=find(parent,x)
    b=find(parent,y)
    if rank[a] > rank[b]:
        parent[b] = a
    elif rank[a] < rank[b]:
        parent[a] = b
    else:
        parent[a] = b
        rank[b]+=1

def printMST(res):
    i,sum=0,0
    n=len(res)
    print(" EDGES \t\tWEIGHTS")
    while i < n:
        src,des,cost=res[i]
        sum+=cost
        print(src,"---->",des,"\t"," ",cost)
        i+=1
    print("Minimum spanning Tree of cost:",sum)


def findMSTKruskal(g,n,res):
    parent=[-1]*n
    rank=[0]*n
    i,j=0,0
    while i < n-1:           
        u,v,w=g[j]
        j+=1
        x=find(parent,u)
        y=find(parent,v)
        if x is not y:
            i+=1
            res.append([u,v,w])
            union(parent,rank,x,y)
    printMST(res)

if __name__ == "__main__":
    g=[]
    addEdge(g,0,1,10)
    addEdge(g,0,2,6)
    addEdge(g,0,3,5)
    addEdge(g,1,3,15)
    addEdge(g,2,3,4)
    # addEdge(g,0,1,1)
    # addEdge(g,0,2,2)
    # addEdge(g,1,2,3)
    # addEdge(g,1,3,1)
    # addEdge(g,1,4,3)
    # addEdge(g,2,3,2)
    # addEdge(g,2,4,1)
    # addEdge(g,3,4,2)
    # addEdge(g,3,5,4)
    # addEdge(g,4,5,3)
    g=sorted(g,key=lambda x: x[2])
    findMSTKruskal(g,4,[])