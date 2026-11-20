from sortedcontainers import SortedSet

T = int(input())

for _ in range(T):
    k = int(input())
    operations = [tuple(input().split()) for _ in range(k)]
    command = [op[0] for op in operations]
    n = [int(op[1]) for op in operations]

    # Please write your code here.
    ss = SortedSet()
    for i in range(k):
        if command[i] == "I":
            ss.add(n[i])
        elif command[i] == "D":
            if len(ss) == 0: continue
            if n[i] == 1:
                ss.remove(ss[-1])
            elif n[i] == -1:
                ss.remove(ss[0])
    if len(ss) == 0:
        print("EMPTY")
    else:
        print(ss[-1], ss[0])
