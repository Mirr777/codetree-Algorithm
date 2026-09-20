n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
arr.sort()

min_answer = float("inf")
for i in range(arr[0]-k,arr[-1]+k+1):
    answer = 0
    for j in range(n):
        if i <= arr[j] <= i + k: continue
        else:
            if abs(i - arr[j]) < abs(i + k - arr[j]):
                answer += abs(i - arr[j])
            else:
                answer += abs(i + k - arr[j])
    min_answer = min(answer, min_answer)
print(min_answer)
