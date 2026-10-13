N, M = map(int, input().split())

# Please write your code here.
path = []
visit = []
def KFC(lev,start):
    if lev == M:
        print(*path)
        return

    for i in range(start,N+1):
        if i in visit: continue
        visit.append(i)
        path.append(i)
        KFC(lev+1,i)
        path.pop()
        visit.pop()

KFC(0,1)
