arr = list(map(int, input().split()))

# Please write your code here.
arr.sort()
A = arr[0]
B = arr[1]
if A + B == arr[2]:
    C = arr[3]
else:
    C = arr[2]
arr.remove(A+B)
arr.remove(A+C)
arr.remove(B+C)
arr.remove(A)
arr.remove(B)
arr.remove(C)
arr.remove(A+B+C)
D = arr[0]
print(A,B,C,D)
