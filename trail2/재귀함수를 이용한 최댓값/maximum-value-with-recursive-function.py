n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
max_answer = 0
answer = 0
def high(n,arr):
    global max_answer
    if n == 0:
        return max_answer
    n = n - 1
    answer = arr[n]
    max_answer = max(answer, max_answer)
    return high(n, arr)


print(high(n,arr))