N = int(input())
moves = [tuple(map(int, input().split())) for _ in range(N)]
a, b = zip(*moves)
a, b = list(a), list(b)

# Please write your code here.
def win_game(moves):
    win_1 = 0
    win_2 = 0
    for i in range(N):
        if moves[i][0] - moves[i][1] == -1 or moves[i][0] - moves[i][1] == 2:
            win_1 += 1
        elif moves[i][0] - moves[i][1] == 1 or moves[i][0] - moves[i][1] == -2: 
            win_2 += 1
    return max(win_1, win_2)
print(win_game(moves))