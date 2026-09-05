ability = list(map(int, input().split()))

# Please write your code here.
ability.sort()
team1 = []
for i in range(3):
    team1.append(ability[i] + ability[-i-1])

answer = max(team1) - min(team1)
print(answer)