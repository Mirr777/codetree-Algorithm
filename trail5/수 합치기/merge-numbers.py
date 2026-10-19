from collections import deque

n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
q = deque()
arr.sort()
a = 0
answer = 0
while True:
    if a == n and len(q) < 2:
        break
    elif a == n and len(q) == 2:
        answer += q[0] + q[1]
        break
    elif a == n and len(q) > 2:
        answer += q[0] + q[1]
        q.append(q[0]+q[1])
        q.popleft()
        q.popleft()
    elif a == n-1 and q == deque():
        break
    elif a == n-1 and len(q) == 1:
        answer += arr[a] + q[0]
        break
    elif a == n-1 and len(q) > 1:
        if arr[a] > q[1]:
            answer += q[0] + q[1]
            q.append(q[0] + q[1])
            q.popleft()
            q.popleft()
        else:
            answer += arr[a] + q[0]
            q.append(arr[a] + q[0])
            q.popleft()
            a += 1
    elif q == deque():
        answer += arr[a] + arr[a+1]
        q.append(arr[a] + arr[a+1])
        a += 2
    elif len(q) == 1:
        if q[0] < arr[a+1]:
            answer += arr[a] + q[0]
            q.append(arr[a] + q[0])
            q.popleft()
            a += 1
        else:
            answer += arr[a] + arr[a+1]
            q.append(arr[a] + arr[a+1])
            a += 2
    elif len(q) > 1:
        if q[0] > arr[a+1]:
            answer += arr[a] + arr[a+1]
            q.append(arr[a] + arr[a+1])
            a += 2
        elif q[1] < arr[a]:
            answer += q[0] + q[1]
            q.append(q[0] + q[1])
            q.popleft()
            q.popleft()
        else:
            answer += arr[a] + q[0]
            q.append(arr[a] + q[0])
            q.popleft()
            a += 1



print(answer)