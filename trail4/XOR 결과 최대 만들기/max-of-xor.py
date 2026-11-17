n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.
path = []
max_answer = 0
def KFC(lev,start):
    global max_answer
    if lev == m:
        answer = 0
        for num in path:
            answer ^= num
        max_answer = max(max_answer, answer)
        return
    for i in range(start,n):
        path.append(A[i])
        KFC(lev+1,i+1)
        path.pop()

KFC(0,0)
print(max_answer)