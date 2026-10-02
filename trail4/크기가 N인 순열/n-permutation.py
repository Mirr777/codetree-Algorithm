n = int(input())

# Please write your code here.
path = []
used = [0] * (n+1)
def permutation(lev):
    if lev == n:
        print(*path)
        return
    for i in range(1,n+1):
        if used[i] == 1: continue
        used[i] = 1
        path.append(i)
        permutation(lev+1)
        path.pop()
        used[i] = 0
permutation(0)