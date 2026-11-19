n = int(input())
words = [input() for _ in range(n)]

# Please write your code here.
d = dict()
max_answer = 1
for i in range(n):
    if words[i] not in d:
        d[words[i]] = 1
    else:
        d[words[i]] += 1
        if d[words[i]] > max_answer:
            max_answer = d[words[i]]

print(max_answer)