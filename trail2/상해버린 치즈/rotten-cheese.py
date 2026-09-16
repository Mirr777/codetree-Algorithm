N, M, D, S = map(int, input().split())

p, m, t = [], [], []
for _ in range(D):
    person, milk, time = map(int, input().split())
    p.append(person)
    m.append(milk)
    t.append(time)

sick_p, sick_t = [], []
for _ in range(S):
    person, time = map(int, input().split())
    sick_p.append(person)
    sick_t.append(time)

# Please write your code here.
milk_set = []
for i in range(D):
    for j in range(S):
        if sick_t[j]-1 >= t[i] and sick_p[j] == p[i]:
            milk_set.append(m[i])
count_milk_set = set()
for a in milk_set:
    if milk_set.count(a) >= S:
        count_milk_set.add(a)

max_answer = 0
for k in count_milk_set:
    answer = set()
    for l in range(D):
        if m[l] == k:
            answer.add(p[l])
    max_answer = max(max_answer, len(answer))
print(max_answer)