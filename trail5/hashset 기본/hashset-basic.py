n = int(input())
commands = []
x = []
for _ in range(n):
    cmd, val = input().split()
    commands.append(cmd)
    x.append(int(val))

# Please write your code here.

A = set()

for i in range(n):
    if commands[i] == "find":
        if x[i] in A:
            print("true")
        else:
            print('false')
    elif commands[i] == "add":
        A.add(x[i])
    elif commands[i] == "remove":
        A.remove(x[i])
