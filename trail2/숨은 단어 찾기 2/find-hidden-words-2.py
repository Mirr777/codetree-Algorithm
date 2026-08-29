N, M = map(int, input().split())
arr = [input() for _ in range(N)]

# Please write your code here.
answer = 0
for i in range(N-2):
    for j in range(M):
        if arr[i][j] == "L":
            if arr[i+1][j] == "E" and arr[i+2][j] == "E":
                answer += 1
        elif arr[i][j] == "E":
            if arr[i+1][j] == "E" and arr[i+2][j] == "L":
                answer +=1
for i in range(N):
    for j in range(M-2):
        if arr[i][j] == "L":
            if arr [i][j+1] == "E" and arr[i][j+2] == "E":
                answer +=1
        elif arr[i][j] == "E":
            if arr[i][j+1] == "E" and arr[i][j+2] == "L":
                answer +=1
for i in range(N-2):
    for j in range(M-2):
        if arr[i][j] == "L":
            if arr[i+1][j+1] == "E" and arr[i+2][j+2] == "E":
                answer += 1
        elif arr[i][j] == "E":
            if arr[i+1][j+1] == "E" and arr[i+2][j+2] == "L":
                answer +=1

for i in range(N-2):
    for j in range(2, M):
        if arr[i][j] == "L":
            if arr[i+1][j-1] == "E" and arr[i+2][j-2] == "E":
                answer +=1
        elif arr[i][j] == "E":
            if arr[i+1][j-1] == "E" and arr[i+2][j-2] == "L":
                answer +=1
print(answer)