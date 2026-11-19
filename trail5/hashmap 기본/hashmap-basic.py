n = int(input())
commands = []
for _ in range(n):
    line = input().split()
    cmd = line[0]
    k = int(line[1])
    if cmd == "add":
        v = int(line[2])
        commands.append((cmd, k, v))
    else:
        commands.append((cmd, k))

# Please write your code here.
d= dict()

for i in range(n):
    if commands[i][0] == "add":
        d[commands[i][1]] = commands[i][2]
    elif commands[i][0] == "find":
        if commands[i][1] in d:
            print(d[commands[i][1]])
        else:
            print("None")
    elif commands[i][0] == "remove":
        d.pop(commands[i][1])