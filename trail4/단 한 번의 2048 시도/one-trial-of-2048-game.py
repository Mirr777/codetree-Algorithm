# Read 4x4 grid
grid = [list(map(int, input().split())) for _ in range(4)]

# Read direction
dir = input()

# Please write your code here.
if dir == "L":
    for i in range(4):
        for j in range(3):
            if grid[i][j] == 0: 
                grid[i][j] = grid[i][j+1]
                grid[i][j+1] = 0
    for i in range(4):
        for j in range(3):
            if grid[i][j] == grid[i][j+1]:
                grid [i][j] = grid[i][j] + grid[i][j]
                grid[i][j+1] = 0
    for k in range(3):
        for i in range(4):
            for j in range(3):
                if grid[i][j] == 0: 
                    grid[i][j] = grid[i][j+1]
                    grid[i][j+1] = 0
elif dir == "R":
    for i in range(4):
        for j in range(1,4):
            if grid[i][-j] == 0:
                grid[i][-j] = grid[i][-j-1]
                grid[i][-j-1] = 0
    for i in range(4):
        for j in range(1,4):
            if grid[i][-j] == grid[i][-j-1]:
                grid [i][-j] = grid[i][-j] + grid[i][-j]
                grid[i][-j-1] = 0
    for k in range(3):
        for i in range(4):
            for j in range(1,4):
                if grid[i][-j] == 0:
                    grid[i][-j] = grid[i][-j-1]
                    grid[i][-j-1] = 0

elif dir == "U":
    for i in range(3):
        for j in range(4):
            if grid[i][j] == 0: 
                grid[i][j] = grid[i+1][j]
                grid[i+1][j] = 0 
    for i in range(3):
        for j in range(4):
            if grid[i][j] == grid[i+1][j]:
                grid [i][j] = grid[i][j] + grid[i][j]
                grid[i+1][j] = 0
    for k in range(3):
        for i in range(3):
            for j in range(4):
                if grid[i][j] == 0: 
                    grid[i][j] = grid[i+1][j]
                    grid[i+1][j] = 0
elif dir == "D":
    for i in range(1,4):
        for j in range(4):
            if grid[-i][j] == 0:
                grid[-i][j] = grid[-i-1][j]
                grid[-i-1][j] = 0
    for i in range(1,4):
        for j in range(4):
            if grid[-i][j] == grid[-i-1][j]:
                grid[-i][j] = grid[-i][j] + grid[-i][j]
                grid[-i-1][j] = 0
    for k in range(3):
        for i in range(1,4):
            for j in range(4):
                if grid[-i][j] == 0:
                    grid[-i][j] = grid[-i-1][j]
                    grid[-i-1][j] = 0

for i in range(4):
    print(*grid[i])
