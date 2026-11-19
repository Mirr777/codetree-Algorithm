n, m = map(int, input().split())

# Note: Using 1-based indexing for words as per C++ code
words = [""] + [input() for _ in range(n)]
queries = [input() for _ in range(m)]

# Please write your code here.

d = dict()
for i in range(n+1):
    d[str(i)] = words[i]
    d[words[i]] = i


for i in range(m):
    print(d[str(queries[i])])