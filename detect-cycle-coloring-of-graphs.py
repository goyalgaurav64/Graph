
                                        #  WRONG ANSWER


from collections import defaultdict 
def createGraph():
    return defaultdict(list)

def addEdge(g,u,v):
    res=-1
    g[u].append(v)

def hasCycleUtil(graph,status,cur):
    if status[cur]==2:
        return True
    flag=False
    status[cur]=1
    for i in range(len(graph[cur])):
        if status[graph[cur][i]]==1:
            status[graph[cur][i]]=2
            # print(status)
        else:
            return hasCycleUtil(graph,status,graph[cur][i])
            
    status[cur]=1
    return False

def hasCycle(graph,v):
    status=[0]*v
    # print(status)
    flag=False
    for i in range(v):
        status[i]=1
        for j in range(len(graph[i])):
            flag=hasCycleUtil(graph,status,graph[i][j])
            if flag==True:
                return True
        status[i]=0
    return False     

if __name__ == "__main__":
    g=createGraph()
    addEdge(g,0,1)
    addEdge(g,1,2)
    addEdge(g,2,3)
    addEdge(g,3,4)
    addEdge(g,4,5)
    print(g)
    ans=hasCycle(g,6)
    if(ans==True):
        print("It has Cycle")
    else:
        print("Does not contain any cycle")