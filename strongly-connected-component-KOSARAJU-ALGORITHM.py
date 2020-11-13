from collections import defaultdict
def createGraph():
    return defaultdict(list)

def addEdge(g,u,v):
    g[u].append(v)

def dfsUtil(g,vis,cur):
    print(cur,end=" ")
    vis[cur]=True
    for i in g[cur]:
        if vis[i] is False:
            dfsUtil(g,vis,i)


def dfsonTransposedGraph(g,vis,s,n):
    for i in range(n):
        vis[i]=False
    print("Following are the Strongly connected Components:")
    while s:
        u=s.pop()
        if vis[u] is False:
            dfsUtil(g,vis,u)
            print()

def transpose(g,gr):
    for i in g:
        for j in g[i]:
            addEdge(gr,j,i)
    return gr

def dfs(g,cur,vis,s):
    vis[cur]=True
    for i in g[cur]:
        if vis[i] is False:
            dfs(g,i,vis,s)
    s.append(cur)

def KosarajubyDFS(g,n):
    s=[]
    vis=[False]*n
    for i in range(n):
        if vis[i] is False:
            dfs(g,i,vis,s)
    
    gr=createGraph()
    gr=transpose(g,gr)
    
    dfsonTransposedGraph(gr,vis,s,n)

if __name__ == "__main__":
    g=createGraph()
    addEdge(g,0,1)
    addEdge(g,1,2)
    addEdge(g,2,0)
    addEdge(g,2,3)
    addEdge(g,3,4)
    addEdge(g,4,5)
    addEdge(g,4,7)
    addEdge(g,5,6)
    addEdge(g,6,4)
    addEdge(g,6,7)

    # addEdge(g,0,2)
    # addEdge(g,0,3)
    # addEdge(g,1,0)
    # addEdge(g,3,4)
    # addEdge(g,2,1)
    
    
    KosarajubyDFS(g,8)