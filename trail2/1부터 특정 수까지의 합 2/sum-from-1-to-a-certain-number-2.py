N = int(input())

# Please write your code here.
answer = 0
def sum(n):
    global answer
    if n == 0:
        return answer
    return answer + n + sum(n-1)
    
print(sum(N))