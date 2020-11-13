from collections import defaultdict
def dfs(g,vis,cur):
    vis[cur]=True
    for i in g[cur]:
        if vis[i] is False:
            dfs(g,vis,i)

def Connections(c,n):
    g=defaultdict(list)
    edges=0
    for i,j in c:
        g[i].append(j)
        g[j].append(i)
        edges+=1

    component=0
    vis=[False] * n
    for i in range(n):
        if vis[i] is False:
            component+=1
            dfs(g,vis,i)
    
    if edges < n-1:
        return -1
    
    re=edges- ((n-1) - (component-1))
    if re >= component-1:
        return component-1
    return -1

if __name__ == "__main__":
    connections=[[0,1],[0,2],[1,2]]
    ans=Connections(connections,4)
    print(ans)