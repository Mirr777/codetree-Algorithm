N = int(input())
heights = [int(input()) for _ in range(N)]

# Please write your code here

heights.sort()
min_answer = float("inf")
for i in range(1, 100):
    answer= 0
    for j in range(N):
        if i <= heights[j] <= i + 17: continue
        else:
            if abs(i - heights[j]) > abs(i + 17  - heights[j]):
                answer += abs(i + 17  - heights[j]) ** 2
            else:
                answer += abs(i - heights[j]) ** 2
    min_answer = min(min_answer, answer)
print(min_answer)