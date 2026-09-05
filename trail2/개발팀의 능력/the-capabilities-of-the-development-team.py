arr = list(map(int, input().split()))

# Please write your code here.
answer = []

for i in range(len(arr)-2):
    for j in range(i+1, len(arr)-1):
        for k in range(len(arr)):
            if (k != i) and (k != j):
                a = sum(arr)-(arr[i]+arr[j]+arr[k])
                b = arr[k]
                c = arr[i]+arr[j]
                if a != b and b != c and c != a:
                    answer.append(max(a,b,c) - min(a,b,c))
if answer == []:
    print(-1)
else:
    print(min(answer))