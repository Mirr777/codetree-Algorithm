n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

d = dict()
answer = 0
visit = []
for i in range(n):
    for j in range(i+1,n):
        diff = k - arr[i] - arr[j]

        if diff in d:
            answer += d[diff]
        
    if arr[i] in d:
        d[arr[i]] += 1
    else:
        d[arr[i]] = 1

print(answer)

    
