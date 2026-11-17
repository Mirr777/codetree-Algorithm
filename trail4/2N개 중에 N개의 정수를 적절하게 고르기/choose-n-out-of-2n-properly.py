n = int(input())
num = list(map(int, input().split()))

# Please write your code here.

path = []
min_answer = float("inf")
def KFC(lev,start):
    global min_answer
    if lev == n:
        answer = sum(path)
        total = sum(num)
        diff = total-answer
        min_answer = min(min_answer, abs(diff-answer))
        return
    
    for i in range(start,n*2):
        path.append(num[i])
        KFC(lev+1,i+1)
        path.pop()

KFC(0,0)
print(min_answer)