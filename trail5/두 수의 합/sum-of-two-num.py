n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
d = dict()
answer = 0
for i in range(n):
    if arr[i] not in d:
        d[arr[i]] = 1
        if k-arr[i] in d and k-arr[i] != arr[i]:
            if d[k-arr[i]] >= 1:
                answer += d[k-arr[i]]
        elif k-arr[i] in d and k-arr[i] == arr[i]:
            answer += d[k-arr[i]] -1
    else:
        d[arr[i]] +=1
        if k-arr[i] in d and k-arr[i] != arr[i]:
            if d[k-arr[i]] >= 1:
                answer += d[k-arr[i]]
        elif k-arr[i] in d and k-arr[i] == arr[i]:
            answer += d[k-arr[i]] -1
print(answer)