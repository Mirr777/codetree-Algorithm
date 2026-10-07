n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

# Please write your code here.
a = n - 1
cnt = 0
while k:
    if k >= coins[a]:
        k -= coins[a]
        cnt +=1
    else:
        a -=1

print(cnt)