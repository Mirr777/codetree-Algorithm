n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.

set1 = set(A) - set(B)
set2 = set(B) - set(A)
print(len(set1) + len(set2))
