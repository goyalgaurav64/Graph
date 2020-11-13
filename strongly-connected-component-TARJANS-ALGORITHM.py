from collections import defaultdict
def createGraph():
    return defaultdict(list)

def addEdge(g,u,v):
    g[u].append(v)

def top(s):
    n=len(s)
    return s[n-1]

def dfs(g,disc,low,Instack,s,time,u):
    disc[u]=low[u]=time
    Instack[u]=True
    s.append(u)
    for v in g[u]:
        if disc[v] is -1:
            dfs(g,disc,low,Instack,s,time+1,v)
            low[u] = min(low[u] , low[v])
        elif Instack[u] is True:
            low[u] = min(low[u] , disc[v])
    
    if low[u] is disc[u]:
        while top(s) != u:
            ele=s.pop()
            Instack[ele]=False
            print(ele,end=" ")
        ele=s.pop()
        Instack[ele]=False
        print(ele,end=" ")
        print()

def SCCTarjans(g,n):
    disc=[-1]*n
    low=[-1]*n
    presentInStack=[False]*n
    s=[]
    for i in range(n):
        if disc[i] is -1:
            dfs(g,disc,low,presentInStack,s,0,i)

if __name__ == "__main__":
    g=createGraph()
    # addEdge(g,0,1)
    # addEdge(g,1,2)
    # addEdge(g,1,3)
    # addEdge(g,3,4)
    # addEdge(g,4,0)
    # addEdge(g,4,5)
    # addEdge(g,4,6)
    # addEdge(g,5,6)
    # addEdge(g,6,5)
    # addEdge(g,5,2)
 
    addEdge(g,0, 1) 
    addEdge(g,0, 3) 
    addEdge(g,1, 2) 
    addEdge(g,1, 4) 
    addEdge(g,2, 0) 
    addEdge(g,2, 6) 
    addEdge(g,3, 2) 
    addEdge(g,4, 5) 
    addEdge(g,4, 6) 
    addEdge(g,5, 6) 
    addEdge(g,5, 7) 
    addEdge(g,5, 8) 
    addEdge(g,5, 9) 
    addEdge(g,6, 4) 
    addEdge(g,7, 9) 
    addEdge(g,8, 9) 
    addEdge(g,9, 8) 

    print("SCC IS:")
    SCCTarjans(g,11)