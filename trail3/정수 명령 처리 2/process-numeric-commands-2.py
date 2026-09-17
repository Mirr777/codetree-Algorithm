N = int(input())
command = []
A = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] == "push":
        A.append(int(line[1]))
    else:
        A.append(0)

# Please write your code here.
que = []
for i in range(N):
    if command[i] == "push":
        que.append(A[i])
    elif command[i] == "front":
        print(que[0])
    elif command[i] == "size":
        print(len(que))
    elif command[i] == "empty":
        if len(que) == 0:
            print(1)
        else:
            print(0)
    elif command[i] == "pop":
        a = que.pop(0)
        print(a)

