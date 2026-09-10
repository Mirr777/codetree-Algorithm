n = int(input())
a, b, c = [], [], []
for _ in range(n):
    num, cnt1, cnt2 = map(int, input().split())
    a.append(num)
    b.append(cnt1)
    c.append(cnt2)

# Please write your code here.
answer = []
answer_set = set()
def count(A,B,C):
    for i in range(111, 1000):
        if str(i)[1] == "0" or str(i)[2] == "0": continue
        elif str(i)[0] == str(i)[1] or str(i)[1] == str(i)[2] or str(i)[0] == str(i)[2]: continue
        r1 = 0
        r2 = 0
        for j in range(3):
            if str(i)[j] == str(A)[j]:
                r1 += 1
            elif str(i)[j] == str(A)[(j+1)%3] or str(i)[j] == str(A)[(j+2)%3]:
                r2 += 1
        if r1 == B and r2 == C:
            answer.append(i)
for i in range(n):
    count(a[i],b[i],c[i])
for j in answer:
    if answer.count(j) == n:
        answer_set.add(j)
print(len(answer_set))
