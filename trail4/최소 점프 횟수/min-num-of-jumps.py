n = int(input())
num = list(map(int, input().split()))

# Please write your code here.
path = []
jump_num = []
def KFC(lev,jump):
    global jump_num
    if n-1 in path:
        jump_num.append(jump)
        return
    for i in range(1,num[lev]+1):
        if lev+i >= n: continue
        path.append(lev+i)
        KFC(lev+i,jump+1)
        path.pop()
KFC(0,0)
if jump_num:
    print(min(jump_num))
else:
    print(-1)