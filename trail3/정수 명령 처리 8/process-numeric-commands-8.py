N = int(input())
command = []
A = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] in ["push_front", "push_back"]:
        A.append(int(line[1]))
    else:
        A.append(0)

# Please write your code here.

stack = []
for i in range(N):
    if command[i] == "push_back":
        stack.append(A[i])
    elif command[i] == "push_front":
        stack = [A[i]] + stack
    elif command[i] == "pop_front":
        a = stack.pop(0)
        print(a)
    elif command[i] == "pop_back":
        b = stack.pop()
        print(b)
    elif command[i] == "size":
        print(len(stack))
    elif command[i] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif command[i] == "front":
        print(stack[0])
    elif command[i] == "back":
        print(stack[-1])