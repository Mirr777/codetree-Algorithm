n = int(input())
numbers = list(map(int, input().split()))

# Please write your code here.
max_number = float("-inf")
answer = 0
for i in range(n-2):
    for j in range(i+2,n):
        answer = numbers[i]+numbers[j]
        if answer > max_number:
            max_number = answer
print(max_number)