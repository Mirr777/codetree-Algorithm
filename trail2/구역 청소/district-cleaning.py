a, b = map(int, input().split())
c, d = map(int, input().split())

# Please write your code here.
def clean(a,b,c,d):
    for i in range(a,b+1):
        for j in range(c,d+1):
            if i == j:
                return max(a,b,c,d) - min(a,b,c,d)
    else:
        return d-c + b - a
print(clean(a,b,c,d))