n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

# Please write your code here.
path = []
dart = [0] * (k+1)
cnt = 0
max_cnt = 0
def KFC(lev):
    global dart
    global cnt
    global max_cnt
    if lev == n:
        for i in range(n):
            dart[path[i]] += nums[i]
        for j in dart:
            if j >= m-1:
                cnt += 1
        max_cnt = max(cnt, max_cnt)
        cnt = 0
        dart = [0] * (k+1)     
        return
    
    for i in range(1,k+1):
        path.append(i)
        KFC(lev+1)
        path.pop()

KFC(0)
print(max_cnt)