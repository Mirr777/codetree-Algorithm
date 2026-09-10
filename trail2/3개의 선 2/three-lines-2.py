n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

# Please write your code here.
def cal(points):
    answer = 0
    for i in range(11):
        for j in range(11):
            for k in range(11):
                answer = 0
                for l in points:
                    if l[0] == i or l[0] == j or l[0] == k:
                        answer += 1
                        if answer == n:
                            return 1
    answer = 0
    for i in range(11):
        for j in range(11):
            for k in range(11):
                answer = 0
                for l in points:
                    if l[1] == i or l[1] == j or l[1] == k:
                        answer += 1
                        if answer == n:
                            return 1
    answer = 0
    for i in range(11):
        for j in range(11):
            for k in range(11):
                answer = 0
                for l in points:
                    if l[0] == i or l[1] == j or l[1] == k:
                        answer += 1
                        if answer == n:
                            return 1
    answer = 0
    for i in range(11):
        for j in range(11):
            for k in range(11):
                answer = 0
                for l in points:
                    if l[1] == i or l[1] == j or l[0] == k:
                        answer += 1
                        if answer == n:
                            return 1
    answer = 0
    for i in range(11):
        for j in range(11):
            for k in range(11):
                answer = 0
                for l in points:
                    if l[1] == i or l[0] == j or l[1] == k:
                        answer += 1
                        if answer == n:
                            return 1
    answer = 0
    for i in range(11):
        for j in range(11):
            for k in range(11):
                answer = 0
                for l in points:
                    if l[1] == i or l[0] == j or l[0] == k:
                        answer += 1
                        if answer == n:
                            return 1
    
    for i in range(11):
        for j in range(11):
            for k in range(11):
                answer = 0
                for l in points:
                    if l[0] == i or l[1] == j or l[0] == k:
                        answer += 1
                        if answer == n:
                            return 1
    
    for i in range(11):
        for j in range(11):
            for k in range(11):
                answer = 0
                for l in points:
                    if l[0] == i or l[0] == j or l[1] == k:
                        answer += 1
                        if answer == n:
                            return 1
    return 0
print(cal(points))