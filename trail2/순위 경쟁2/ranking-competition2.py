n = int(input())
c = []
s = []
for _ in range(n):
    ci, si = input().split()
    c.append(ci)
    s.append(int(si))

# Please write your code here.
dart = [0] * 2
mode = 3
answer = 0
for i in range(n):
    if c[i] == "A":
        dart[0] += s[i]
        if dart[0] > dart[1]:
            if mode != 1:
                mode = 1
                answer +=1
        elif dart[0] < dart[1]:
            if mode != 2:
                mode = 2
                answer +=1
        elif dart[0] == dart[1]:
            if mode != 3:
             mode = 3
             answer +=1
    else:
        dart[1] += s[i]
        if dart[0] > dart[1]:
            if mode != 1:
                mode = 1
                answer +=1
        elif dart[0] < dart[1]:
            if mode != 2:
                mode = 2
                answer +=1
        elif dart[0] == dart[1]:
            if mode != 3:
             mode = 3
             answer +=1
print(answer)