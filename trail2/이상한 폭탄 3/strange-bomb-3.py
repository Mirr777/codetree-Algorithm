N, K = map(int, input().split())
num = [int(input()) for _ in range(N)]

# Please write your code here.
max_answer = 0
final_answer = 0
for i in range(N):
    answer = set()
    answer_list = {i}
    for j in range(i+1,N):
        if num[i] == num[j]:
            answer_list.add(j)
        for k in range(len(answer_list)-1):
            if list(answer_list)[k+1] - list(answer_list)[k] <= K:
                answer.add(k)
                answer.add(k+1)
    if len(answer) > max_answer and final_answer < num[i]:
        max_answer = max(max_answer,len(answer))
        final_answer = num[i]
print(final_answer)