K, N = map(int, input().split())

# Please write your code here.
path = []
def KFC(lev):
    if lev == N:
        print(*path)
        return
    for i in range(1,K+1):
        path.append(i)
        KFC(lev+1)
        path.pop()

KFC(0)