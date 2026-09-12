n = int(input())
ranges = [tuple(map(int, input().split())) for _ in range(n)]
a, b = zip(*ranges)
a, b = list(a), list(b)

# Please write your code here.
def one(n,ranges):
    for i in range(10001):
        for j in range(n):
            if ranges[j][0]<=(2**(j+1))*i<= ranges[j][1]:continue
            else:break
        else:
            return i
print(one(n,ranges))