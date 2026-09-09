N = int(input())

# Please write your code here.
def square(n):
    if n == 0:
        return 0
    return (n % 10) ** 2 + square(n//10)
    

print(square(N))