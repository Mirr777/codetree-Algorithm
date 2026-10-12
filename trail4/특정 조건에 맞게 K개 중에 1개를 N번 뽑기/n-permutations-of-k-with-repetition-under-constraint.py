K, N = map(int, input().split())

# Please write your code here.
path = []
def KFC(lev):
    if lev == N:
        print(*path)
        return
    for i in range(1,K+1):
        if len(path) >= 2:
            if path[-1] == i and path[-2] == i: continue
        path.append(i)
        KFC(lev+1)
        path.pop()

KFC(0)