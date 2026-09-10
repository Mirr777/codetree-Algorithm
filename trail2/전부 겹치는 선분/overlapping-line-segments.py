n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
x1, x2 = zip(*segments)
x1, x2 = list(x1), list(x2)

# Please write your code here.
dart = [0] * 101
def line(segments, n):
    for i in range(n):
        for j in range(segments[i][0], segments[i][1]+1):
            dart[j] += 1
    for k in dart:
        if k == n:
            return "Yes"
    return "No"
print(line(segments, n))