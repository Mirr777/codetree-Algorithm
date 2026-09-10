n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
x1 = [seg[0] for seg in segments]
x2 = [seg[1] for seg in segments]

# Please write your code here.
def line(n,segments):
    for i in range(n):
        dart = [0] * 101
        for j in range(n):
            if i == j: continue
            for k in range(segments[j][0], segments[j][1]+1):
                dart[k] += 1
        for l in dart:
            if l == n-1:
                return "Yes"
    return "No"


print(line(n,segments))