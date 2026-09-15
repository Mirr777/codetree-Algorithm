arr = list(map(int, input().split()))

# Please write your code here.
arr.sort()
A = arr[0]
B = arr[1]
if arr[2] == A+B:
    C = arr[3]
else:
    C = arr[2]
print(A,B,C)