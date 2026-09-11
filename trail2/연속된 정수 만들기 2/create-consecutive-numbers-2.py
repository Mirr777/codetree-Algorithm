pos = list(map(int, input().split()))

# Please write your code here.
def seq(pos):
    if (abs(pos[0]- pos[1]) == 1 and abs(pos[1]-pos[2]) == 1) or (abs(pos[0]- pos[2]) == 1 and abs(pos[2]-pos[1]) == 1) or (abs(pos[0]- pos[2]) == 1 and abs(pos[0]-pos[1]) == 1) :
        return 0
    elif abs(pos[0]- pos[1]) == 2:
        return 1
    elif abs(pos[1]-pos[2]) == 2:
        return 1
    else:
        return 2
print(seq(pos))