from collections import defaultdict
def createGraph():
    g=defaultdict(list)
    return g


def topoSort(g,indeg,q,cnt,n,res):
    for i in range(n):
        if indeg[i] is 0:
            q.append(i)
    while(q):
        cur=q.pop(0)
        for i in g[cur]:
            indeg[i]-=1
            if(indeg[i] is 0):
                q.append(i)
        res.append(cur)
        cnt+=1
    if cnt is n:
        return True
    return False

def kahnsAlgo(g,indeg,n):
    q,res=[],[]
    if topoSort(g,indeg,q,0,n,res) is True:
        return res
    return []

if __name__ == "__main__":
    # prequisites=[[1,0],[2,0],[3,1],[3,2]]
    prequisites=[[1,0],[2,1],[3,2],[1,3]]
    g=createGraph()
    n=4
    indeg=[0]*n
    for i,j in prequisites:
        g[j].append(i)
        indeg[i]+=1
    ans=kahnsAlgo(g,indeg,n)
    print(ans)