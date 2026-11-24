n, m = map(int, input().split())

A = [input() for _ in range(n)]
B = [input() for _ in range(n)]

# Please write your code here.
answer = 0
path = []

def KFC(lev,start):
    global answer
    if lev == 3:
        set1 = set()
        set2 = set()
        for i in range(n):
            answer1 = ""
            answer2 = ""
        
            for j in path:
                answer1 += A[i][j]
                answer2 += B[i][j]
            set1.add(answer1)
            set2.add(answer2)
        if len(set1) + len(set2) == len(set1|set2):
            answer += 1
        
        return
    for i in range(start, m):
        path.append(i)
        KFC(lev+1,i+1)
        path.pop()
KFC(0,0)
print(answer)