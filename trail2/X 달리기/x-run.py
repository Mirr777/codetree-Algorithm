X = int(input())

# Please write your code here.
answer = 0
peak = 0
for i in range(1,X//2+1):
    peak = i-1
    if answer >= X//2:
        break
    answer += i

space = 0
for i in range(peak+1):
    space += i
if X <= 3:
    print(X)

elif X <= space * 2 - i:
    print(peak*2-1)
else:
    print(peak*2)
