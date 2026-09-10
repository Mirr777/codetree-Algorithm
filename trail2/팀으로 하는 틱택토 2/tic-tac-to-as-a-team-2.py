inp = [input() for _ in range(3)]

# Please write your code here.
answer = []
list_inp = list(map(list,inp))

for i in range(3):
    A = set()
    B = set()
    for j in range(3):
        A.add(list_inp[i][j])
        B.add(list_inp[j][i])
    if len(A) == 2:
        answer.append(A)
    if len(B) == 2:
        answer.append(B)
C = set()
D = set()
for k in range(3):
    C.add(list_inp[k][k])
    D.add(list_inp[2-k][k])
if len(C) == 2:
    answer.append(C)
if len(D) == 2:
    answer.append(D)
if len(answer) == 0:
    final_answer = 0
else:
    final_answer = 1
for i in range(len(answer)):
    if answer[0] == answer[i]: continue
    final_answer += 1
print(final_answer)