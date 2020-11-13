def dfs(g,cur,res,li):
    if cur is len(g)-1:
        res.append(li.copy())
        return
    for i in g[cur]:
        li.append(i)
        dfs(g,i,res,li)
        li.pop()

def NoOfPaths(graph):
    res,li=[],[]
    li.append(0)
    dfs(graph,0,res,li)
    return res

if __name__ == "__main__":
    graph=[[4,3,1],[3,2,4],[3],[4],[]]
    ans=NoOfPaths(graph)
    print(ans)