N, H, T = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
min_value = float("inf")
answer = 0
for i in range(N-T+1):
    answer = 0
    for j in range(T):
        answer += abs(H - arr[i+j])
    if min_value > answer:
        min_value = answer
print(min_value)
