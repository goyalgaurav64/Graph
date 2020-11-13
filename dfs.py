from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
    
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def dfs(self,s,visited):
        visited[s]=True
        print(s,end=" ")

        for i in self.graph[s]:
            if visited[i]==False:
                self.dfs(i,visited)

    def helper(self,s):           #  s -> Starting Vertex
        visited=[False]*len(self.graph)
        self.dfs(s,visited)

if __name__ == "__main__":
    g=Graph()
    g.addEdge(0,1)
    g.addEdge(0,2)
    g.addEdge(1,2)
    g.addEdge(2,0)
    g.addEdge(2,3)
    g.addEdge(3,3)

    # visited=[False]*(max(g.graph)+1)
    # g.dfs(2,visited)
    g.helper(2)