from collections import defaultdict
import sys
def createGraph(a):
    g=defaultdict(list)
    for i,j,k in a:
        g[i].append((j,k))
    return g

def dfsUtil(g,src,des,k,cost):
    fare=sys.maxsize
    if src==des:
        fare=min(fare,cost)
        return 0
    if k == 0:
        return
    # vis[src]=True
    for nei,cst in g[src]:
        if cst+cost >= fare:
            continue
        dfsUtil(g,nei,des,k-1,cst+cost)
    # print(fare)
    return fare if fare is not sys.maxsize else -1

def dfs(g):
    return dfsUtil(g,0,2,k+1,0)
    




if __name__ == "__main__":
    a=[[0,1,100],[1,2,100],[0,2,500]]
    g=createGraph(a)
    k=1
    
    ans=dfs(g)
    print(ans)