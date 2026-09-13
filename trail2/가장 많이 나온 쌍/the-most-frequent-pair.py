n, m = map(int, input().split())
pairs = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
max_answer = 0
for i in range(1,n+1):
    for j in range(i+1,n+1):
        answer = 0
        for k in range(m):
            if pairs[k] == (i,j) or pairs[k] == (j,i):
                answer +=1
        max_answer = max(answer,max_answer)
print(max_answer)