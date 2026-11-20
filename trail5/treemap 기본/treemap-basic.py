from sortedcontainers import SortedDict

n = int(input())

cmd = []
k = []
v = []

for _ in range(n):
    line = input().split()
    cmd.append(line[0])
    if line[0] == "add":
        k.append(int(line[1]))
        v.append(int(line[2]))
    elif line[0] == "remove" or line[0] == "find":
        k.append(int(line[1]))
        v.append(0)
    else:
        k.append(0)
        v.append(0)

# Please write your code here.

sd = SortedDict()

for i in range(n):
    if cmd[i] == "add":
        sd[k[i]] = v[i]
    elif cmd[i] == "find":
        if k[i] in sd:
            print(sd[k[i]])
        else:
            print("None")
    elif cmd[i] == "remove":
        sd.pop(k[i])
    elif cmd[i] == "print_list":
        if len(sd) == 0:
            print("None")
        else:
            for key, value in sd.items():
                print(value, end = " ")
            print()
    
