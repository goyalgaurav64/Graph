from collections import defaultdict
def createGraph(prequisites):
    g=defaultdict(list)
    for i,j in prequisites:
        g[j].append(i)
    return g


def hasCycleUtil(g,vis,cur):
    vis[cur]=1
    for i in g[cur]:
        if vis[i]==1:
            return True
        if vis[i]==0 and hasCycleUtil(g,vis,i):
            return True
    vis[cur]=2
    return False

def hasCycle(g,n):
    vis=[0]*n
    for i in range(n):
        if vis[i]==0:
            if hasCycleUtil(g,vis,i):
                return True
    return False

def dfs(g,cur,vis,res):
    vis[cur]=True
    for i in g[cur]:
        if vis[i]==False:
            dfs(g,i,vis,res)
    res.append(cur)

def topoSort(g,n):
    res=[]
    vis=[False]*n
    if(hasCycle(g,n)):
        return res
    for i in range(n):
        if vis[i]==False:
            dfs(g,i,vis,res)
    return res[::-1]


if __name__ == "__main__":
    # prequisites=[[1,0],[2,0],[3,1],[3,2]]
    prequisites=[[1,0]]
    g=createGraph(prequisites)
    ans=topoSort(g,2)
    print(ans)