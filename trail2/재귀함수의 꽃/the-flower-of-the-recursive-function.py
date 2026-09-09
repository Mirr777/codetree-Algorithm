N = int(input())

# Please write your code here.

def flower(n):
    if n == 0:
        return
    print(n, end = " ")
    flower(n-1)
    print(n, end = " ")
flower(N)