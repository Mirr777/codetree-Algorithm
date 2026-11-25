n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
answer = []
d = dict()
max_answer = 0
for i in range(n):
    if arr[i] in d:
        d[arr[i]] += 1
    else:
        d[arr[i]] = 1

for key, value in sorted(d.items(), key = lambda x : (-x[1], -x[0])):
    answer.append(key)

for i in range(k):
    print(answer[i], end= " ")