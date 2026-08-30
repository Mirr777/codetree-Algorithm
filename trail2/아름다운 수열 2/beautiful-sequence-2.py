N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
answer = 0
pop_list = B[:]
for i in range(N-M+1):
    pop_list = B[:]
    for j in range(M):
        if A[i+j] not in pop_list:
            break
        else:
            pop_list.pop(pop_list.index(A[i+j]))
    else:
        answer +=1
print(answer)