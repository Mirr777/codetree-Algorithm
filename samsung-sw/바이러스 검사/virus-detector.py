N = int(input())
arr = list(map(int,input().split()))
A,B = map(int,input().split())

answer = 0
arr2 = []
for i in arr:
    if i-A <= 0:
        answer += 1
    else:
        answer += 1
        arr2.append(i-A)

for i in arr2:
    if i % B == 0:
        answer += i // B
    else:
        answer += i // B + 1

print(answer)

