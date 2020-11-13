def doTransformation(list,startWord,endWord):
    if endWord not in list:
        return -1
    list=set(list)
    q=[]
    q.append([startWord,1])
    while q:
        cur , length = q.pop(0)
        if cur == endWord:
            return length
        for i in range(len(cur)):
            for j in 'abcdefghijklmnopqrstuvwxyz':
                nextWord = cur[:i] + j + cur[i+1:]
                if nextWord in list:
                    list.remove(nextWord)
                    q.append([nextWord,length+1])
    return 0

if __name__ == "__main__":
    wordList=["hot","dot","dog","lot","log","cog"]
    ans=doTransformation(wordList,"hit","cog")
    if ans is not -1:
        print("Minimum steps required to transfrom is:",ans)
    else:
        print("Transformation is not possible")