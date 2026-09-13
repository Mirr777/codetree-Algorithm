n = int(input())
l = []
r = []
for _ in range(n):
    left, right = map(int, input().split())
    l.append(left)
    r.append(right)

# Please write your code here.
answer = 0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            dart = []
            for m in range(n):
                if m== i or m == k or m == j: continue
                for o in range(l[m], r[m]+1):
                    dart.append(o)
            if len(dart) == len(set(dart)):
                answer +=1
print(answer)