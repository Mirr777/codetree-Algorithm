from sortedcontainers import SortedDict

n = int(input())
words = [input() for _ in range(n)]

# Please write your code here.

sd = SortedDict()
full = 0
for i in range(n):
    if words[i] not in sd:
        sd[words[i]] = 1
        full += 1
    else:
        sd[words[i]] += 1
        full += 1


for key, value in sd.items():
    x = value/full * 100
    print(f"{key} {x:.4f}")
