from sortedcontainers import SortedDict

n = int(input())
words = [input() for _ in range(n)]

# Please write your code here.

sd = SortedDict()

for i in range(n):
    if words[i] not in sd:
        sd[words[i]] = 1
    else:
        sd[words[i]] += 1

for k, v in sd.items():
    print(k, v)