n, t = map(int, input().split())

l = list(map(int, input().split()))
r = list(map(int, input().split()))
d = list(map(int, input().split()))

# Please write your code here.

cnt = t 
while True:
    if cnt == 0:
        break
    new_l = [d[n-1]]
    new_r = [l[n-1]]
    new_d = [r[n-1]]
    for i in range(n-1):
        new_l.append(l[i])
        new_r.append(r[i])
        new_d.append(d[i])
    cnt -= 1
    l = new_l
    r = new_r
    d = new_d
print(*l)
print(*r)
print(*d)