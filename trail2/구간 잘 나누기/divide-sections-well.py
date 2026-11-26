n, m = map(int, input().split())
a = list(map(int, input().split()))

# Please write your code here.

for i in range(max(a), sum(a)):
    answer = 0
    count = 0
    for j in range(n):
        if a[j] + answer <= i: 
            answer += a[j]
        else:
            count += 1
            answer = a[j]
    count += 1
    if count <= m:
        print(i)
        break
