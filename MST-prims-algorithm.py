#                           TIME COMPLEXITY : O(V)^2
import sys

def printMST(g,parent,n):
    # print(parent)
    print(" EDGES \tWEIGHTS")
    sum=0
    for i in range(1,n):
        sum+=g[i][parent[i]]
        print(parent[i],"->",i,"\t  ",g[i][parent[i]]) 
    print("Sum of weights is:",sum)
def findMinNode(w,set,n):
    min=sys.maxsize
    v=-1
    for i in range(n):
        if set[i] is False and min > w[i]:
            min=w[i]
            v=i
    return v

def findMSTPrims(g,n):
    weight=[sys.maxsize]*n
    mstSET=[False]*n
    parent=[None]*n
    parent[0]=-1
    weight[0]=0
    for i in range(n):
        u=findMinNode(weight,mstSET,n)
        mstSET[u]=True
        for j in range(n):
            if g[u][j] > 0 and mstSET[j] is False and weight[j] > g[u][j]:
                weight[j] = g[u][j]
                parent[j] = u
    printMST(g,parent,n)



if __name__ == "__main__":
    # graph=[ [0, 2, 0, 6, 0], 
    #         [2, 0, 3, 8, 5], 
    #         [0, 3, 0, 0, 7], 
    #         [6, 8, 0, 0, 9], 
    #         [0, 5, 7, 9, 0]]
    graph=[[0,4,6,0,0,0],
    [4,0,6,3,4,0],
    [6,6,0,1,8,0],
    [0,3,1,0,2,3],
    [0,4,8,2,0,7],
    [0,0,0,3,7,0]]
    v=6
    findMSTPrims(graph,v) 