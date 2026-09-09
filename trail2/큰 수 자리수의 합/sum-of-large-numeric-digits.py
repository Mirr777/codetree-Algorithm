a, b, c = map(int, input().split())

# Please write your code here.
def three(n):
    if n == 0:
        return 0
    return three(n//10) + n % 10
n = a * b * c
print(three(n))