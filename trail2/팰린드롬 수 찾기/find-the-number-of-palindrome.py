X, Y = map(int, input().split())

# Please write your code here.
def pellindrome(n):
    if str(n) == str(n)[::-1]:
        return 1
    else:
        return 0
answer = 0
for i in range(X, Y+1):
    answer += pellindrome(i)
print(answer)