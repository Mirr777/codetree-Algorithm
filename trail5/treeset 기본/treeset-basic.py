from sortedcontainers import SortedSet

n = int(input())
command = []
x = []

for _ in range(n):
    line = input().split()
    command.append(line[0])
    if line[0] in ["add", "remove", "find", "lower_bound", "upper_bound"]:
        x.append(int(line[1]))
    else:
        x.append(0)

# Please write your code here.

ss = SortedSet()

for i in range(n):
    if command[i] == "add":
        ss.add(x[i])
    elif command[i] == "remove":
        ss.remove(x[i])
    elif command[i] == "find":
        if x[i] in ss:
            print("true")
        else:
            print("false")
    elif command[i] == "lower_bound":
        idx = ss.bisect_left(x[i])
        if len(ss) >= idx + 1:
            print(ss[idx])
        else:
            print("None")
    elif command[i] == "upper_bound":
        idx = ss.bisect_right(x[i])
        if len(ss) >= idx + 1:
            print(ss[idx])
        else:
            print("None")
    elif command[i] == "largest":
        if len(ss) == 0:
            print("None")
        else:
            print(ss[-1])
    elif command[i] == "smallest":
        if len(ss) == 0:
            print("None")
        else:
            print(ss[0])
