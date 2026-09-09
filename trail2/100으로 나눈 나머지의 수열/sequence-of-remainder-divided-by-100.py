N = int(input())

# Please write your code here.
def hundred(n):
    if n == 1:
        return 2
    elif n == 2:
        return 4
    else:
        return (hundred(n-1) * hundred(n-2)) % 100

print(hundred(N))