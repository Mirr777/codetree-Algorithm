n = int(input())

# Please write your code here.
count = 0
def recursive(N):
    global count
    if N == 1:
        return
    elif N % 2== 0:
        count += 1
        recursive(N//2)
    elif N % 2 == 1:
        count += 1
        recursive(N*3 + 1)

recursive(n)
print(count)