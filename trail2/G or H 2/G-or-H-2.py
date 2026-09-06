n = int(input())
people = [tuple(input().split()) for _ in range(n)]
pos = [int(p[0]) for p in people]
alpha = [p[1] for p in people]

# Please write your code here.
people.sort(key = lambda x : int(x[0]))
answer = []
G_count = 0
H_count = 0
for i in range(n):
    for j in range(i+1,n):
        G_count = 0
        H_count = 0
        for k in range(i,j+1):
            if people[k][1] == "G":
                G_count +=1
                if G_count == H_count or H_count == 0:
                    answer.append(int(people[k][0])-int(people[i][0]))
            else:
                H_count +=1
                if G_count == H_count or G_count == 0:
                    answer.append(int(people[k][0])-int(people[i][0]))
if answer == []:
    print(0)
else:
    print(max(answer))
            