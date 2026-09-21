n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

arr.sort()

answer1 = arr[-1] * arr[-2] * arr[-3]
answer2 = arr[0] * arr[1] * arr[-1]

print(max(answer1,answer2))