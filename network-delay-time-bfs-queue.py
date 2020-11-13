import sys
from collections import defaultdict
def createGraph(times):
    g=defaultdict(list)
    for u,v,w in times:
        g[u].append((v,w))
    return g

def networkDelayTime(g,n,k):
    q=[]
    dist=[sys.maxsize]*(n+1)
    dist[k]=0
    q.append([k,0])
    while q:
        node,wt=q.pop(0)
        for v,w in g[node]:
            if dist[v] >  w + wt:
                dist[v] =  w + wt
                q.append([v,w + wt])
    m=-1
    for i in range(1,n+1):
        if dist[i] is sys.maxsize:
            return -1
        m=max(m,dist[i])
    return m


if __name__ == "__main__":
    # times=[[2,1,1],[2,3,1],[3,4,1]]
    # times=[[1,2,1],[1,3,2],[2,4,4],[2,5,5],[3,5,3]]
    times=[[3,5,78],[2,1,1],[1,3,0],[4,3,59],[5,3,85],[5,2,22],[2,4,23],[1,4,43],[4,5,75],[5,1,15],[1,5,91],[4,1,16],[3,2,98],[3,4,22],[5,4,31],[1,2,0],[2,5,4],[4,2,51],[3,1,36],[2,3,59]]
    n,k=5,5
    g=createGraph(times)
    ans=networkDelayTime(g,n,k)
    print(ans)