from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
    
    def addEdge(self,u,v):
        self.graph[u].append(v)

    def hasCycleUtil(self,graph,visited,cur):
        if  visited[cur]==True:
            return True
        visited[cur]=True
        flag=False
        for i in range(len(self.graph[cur])):
            flag=self.hasCycleUtil(graph,visited,graph[cur][i])
            if flag==True:
                return True
        visited[cur]=False
        return False
    
    def hasCycle(self,v,graph):
        visited=[False]*v
        flag=False
        for i in range(v):
            visited[i]=True
            for j in range(len(self.graph[i])):
                # print(graph[i][j])
                flag=self.hasCycleUtil(graph,visited,graph[i][j])
                # print(flag)
                if(flag==True):
                    return True
            visited[i]=False
        return False
g=Graph()
# g.addEdge(0,1)
# g.addEdge(1,2)
# g.addEdge(2,3)
# g.addEdge(3,4)
# g.addEdge(4,5)

# g.addEdge(0,1)
# g.addEdge(2,1)
# g.addEdge(2,3)
# g.addEdge(3,4)
# g.addEdge(4,0)
# g.addEdge(4,2)

g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(2,3)
# g.addEdge(4,0)
# g.addEdge(4,2)

n=len(g.graph)+1
ans=g.hasCycle(n,g.graph)
if(ans==True):
    print("It has Cycle")
else:
    print("Does not contain any cycle")
