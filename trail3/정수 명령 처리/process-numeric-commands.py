N = int(input())
command = []
value = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] == "push":
        value.append(int(line[1]))
    else:
        value.append(0)

# Please write your code here.
stack = []
for i in range(N):
    if command[i] == "push":
        stack.append(value[i])
    elif command[i] == "size":
        print(len(stack))
    elif command[i] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif command[i] == "pop":
        a = stack.pop()
        print(a)
    elif command [i] == "top":
        print(stack[-1])