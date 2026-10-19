n = int(input())
price = list(map(int, input().split()))

# Please write your code here.
a = float("inf")
max_answer = 0
for i in price:
    if a > i:
        a = i
    else:
        answer = i-a
        max_answer = max(answer, max_answer)
print(max_answer)
