X, Y = map(int, input().split())

# Please write your code here.
def strange(n):
    a = str(n)
    count = 0
    for i in range(len(a)-1):
        for j in range(i+1,len(a)):
            if a[i] != a[j]:
                count += 1
    if count == len(a) - 1:
        return 1
    else:
        return 0
answer = 0

for i in range(X, Y+1):
    answer += strange(i)
print(answer)