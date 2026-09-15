x1, y1, x2, y2 = map(int, input().split())
a1, b1, a2, b2 = map(int, input().split())

# Please write your code here.
a ,b,c,d = min(x1,a1), min(y1,b1), max(x2,a2), max(y2,b2)
e = max(c-a, d-b)
print(e**2)