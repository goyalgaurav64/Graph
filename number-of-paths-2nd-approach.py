def dfs(g,cur,res,li):
    if cur is len(g)-1:
        res.append(li)
        return
    for i in g[cur]:
        dfs(g,i,res,li+[i])

def NoOfPaths(graph):
    res=[]
    dfs(graph,0,res,[0])
    return res

if __name__ == "__main__":
    graph=[[4,3,1],[3,2,4],[3],[4],[]]
    ans=NoOfPaths(graph)
    print(ans)