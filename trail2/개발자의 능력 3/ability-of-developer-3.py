abilities = list(map(int, input().split()))

# Please write your code here.
answer = float("inf")
sum_list = 0
for i in range(len(abilities)-2):
    for j in range(i+1, len(abilities)-1):
        for k in range(j+1, len(abilities)):
            sum_list = abilities[i]+abilities[j]+abilities[k]
            answer = min(answer, abs((sum(abilities)-sum_list) - sum_list))

print(answer)