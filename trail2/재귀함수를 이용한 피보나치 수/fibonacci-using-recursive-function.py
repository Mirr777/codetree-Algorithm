N = int(input())

# Please write your code here.

def piv(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return piv(n-2) + piv(n-1)
print(piv(N))