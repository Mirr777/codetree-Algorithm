n = int(input())
cmd = []
num = []

for _ in range(n):
    line = input().split()
    cmd.append(line[0])
    if line[0] in ["push_front", "push_back"]:
        num.append(int(line[1]))
    else:
        num.append(0)

# Please write your code here.

deck = []
for i in range(n):
    if cmd[i] == "push_back":
        deck.append(num[i])
    elif cmd[i] == "push_front":
        deck = [num[i]] + deck
    elif cmd[i] == "pop_back":
        a = deck.pop()
        print(a)
    elif cmd[i] == "pop_front":
        b = deck.pop(0)
        print(b)
    elif cmd[i] == "size":
        print(len(deck))
    elif cmd[i] == "empty":
        if len(deck) == 0:
            print(1)
        else:
            print(0)
    elif cmd[i] == "front":
        print(deck[0])
    elif cmd[i] == "back":
        print(deck[-1])