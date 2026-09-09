N = int(input())

# Please write your code here.

def prog(N):
    if N % 2 == 1:
        if N == 1:
            return 1
        else:
            return N + prog(N-2)
    else:
        if N == 2:
            return 2
        else:
            return N + prog(N-2)
print(prog(N))
    