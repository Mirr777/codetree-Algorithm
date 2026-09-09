n = int(input())

# Please write your code here.
def star(N):
    if N == 0:
        return
    print("* " * N)
    star(N-1)
    print("* " * N)

star(n)
