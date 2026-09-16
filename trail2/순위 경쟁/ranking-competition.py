n = int(input())
c, s = [], []
for _ in range(n):
    ci, si = input().split()
    c.append(ci)
    s.append(int(si))

# Please write your code here.
A = [0,0,0]
answer = 0
for i in range(n):
    top1 = []
    top2 = []
    for j in range(3):
        if A[j] == max(A):
            top1.append(j)
    if c[i] == "A":
        A[0] += s[i]
    elif c[i] == "B":
        A[1] += s[i]
    elif c[i] == "C":
        A[2] += s[i]
    a = A.count(max(A))
    for k in range(3):
        if A[k] == max(A):
            top2.append(k)
    if top1 != top2:
        answer += 1 
print(answer)