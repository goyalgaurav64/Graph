from collections import defaultdict
def createGraph(tickets):
    g=defaultdict(list)
    for src,des in tickets:
        if src in g:
            g[src].append(des)
        else:
            g[src]=[des]
    print(g)
    for i in g.keys():
        g[i].sort(reverse=True)
    return g

def reconstructRoute(g):
    s=[]
    res=[]
    s.append("JFK")
    while len(s) > 0:
        ele=s[-1]
        if ele in g and len(g[ele])>0:
            s.append(g[ele].pop())
        else:
            res.append(s.pop())
    return res[::-1]


if __name__ == "__main__":
    tickets=[["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    g=createGraph(tickets)
    ans=reconstructRoute(g)
    print(ans)