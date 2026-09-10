x1, x2, x3, x4 = map(int, input().split())

# Please write your code here.
def intersecting(x1,x2,x3,x4):
    for i in range(x1,x2+1):
        if i == x3 or i == x4:
            return "intersecting"
    for j in range(x3,x4+1):
        if j == x1 or j == x2:
            return "intersecting"
    return "nonintersecting"
print(intersecting(x1,x2,x3,x4))