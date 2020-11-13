from collections import defaultdict
def createGraph():
    g=defaultdict(list)
    return g

def addEdge(g,u,v):
    g[u].append(v)

def hasCycleUtil(graph,visited,cur):
    if  visited[cur]==True:
        return True
    visited[cur]=True
    flag=False
    for i in range(len(graph[cur])):
        flag=hasCycleUtil(graph,visited,graph[cur][i])
        if flag==True:
            return True
    visited[cur]=False
    return False
    
def hasCycle(graph,v):
    visited=[False]*v
    print(visited)
    flag=False
    for i in range(v):
        visited[i]=True
        for j in range(len(graph[i])):
            # print(graph[i][j])
            flag=hasCycleUtil(graph,visited,graph[i][j])
            # print(flag)
            if(flag==True):
                return True
        visited[i]=False
    return False

if __name__ == "__main__":
    g=createGraph()
    addEdge(g,0,1)
    addEdge(g,1,2)
    addEdge(g,2,3)
    addEdge(g,3,4)
    addEdge(g,4,5)

    # addEdge(g,0,1)
    # addEdge(g,1,2)
    # addEdge(g,2,3)
    # addEdge(g,3,4)
    # addEdge(g,4,2)

    # addEdge(g,0,1)
    # addEdge(g,2,1)
    # addEdge(g,2,3)
    # addEdge(g,3,4)
    # addEdge(g,4,0)
    # addEdge(g,4,2)
    print(g)
    ans=hasCycle(g,len(g)+1)
    if(ans==True):
        print("It has Cycle")
    else:
        print("Does not contain any cycle")