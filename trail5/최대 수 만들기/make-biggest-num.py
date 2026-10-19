from functools import cmp_to_key

n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.

def compare(x,y):
    
    if str(x) + str(y) > str(y) + str(x):
        return -1
    elif str(x) + str(y) < str(y) + str(x):
        return 1
    return 0

arr.sort(key = cmp_to_key(compare))

for i in arr:
    print(i, end = "")

