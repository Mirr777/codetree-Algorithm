board = [list(map(int, input().split())) for _ in range(19)]

# Please write your code here.
answer = 0
for i in range(2,17):
    for j in range(2,17):
        if board[i][j] == 1:
            if board[i+1][j+1] == 1 and board[i+2][j+2] == 1 and board[i-1][j-1] == 1 and board[i-2][j-2] == 1:
                answer = 1
                print(answer)
                print(i+1,j+1)
                break
            elif board[i+1][j-1] == 1 and board[i+2][j-2] == 1 and board[i-1][j+1] == 1 and board[i-2][j+2] == 1:
                answer = 1
                print(answer)
                print(i+1,j+1)
                break

        elif board[i][j] == 2:
            if board[i+1][j+1] == 2 and board[i+2][j+2] == 2 and board[i-1][j-1] == 2 and board[i-2][j-2] == 2:
                answer = 2
                print(answer)
                print(i+1,j+1)
                break
            elif board[i+1][j-1] == 2 and board[i+2][j-2] == 2 and board[i-1][j+1] == 2 and board[i-2][j+2] == 2:
                answer = 2
                print(answer)
                print(i+1,j+1)
                break    

for i in range(19):
    for j in range(2,17):
        if board[i][j] == 1:
            if board[i][j-1] == 1 and board[i][j-2] == 1 and board[i][j+1] == 1 and board[i][j+2] == 1:
                answer = 1
                print(answer)
                print(i+1,j+1)
                break

        elif board[i][j] == 2:
            if board[i][j+1] == 2 and board[i][j+2] == 2 and board[i][j-1] == 2  and board[i][j-2] == 2:
                answer = 2
                print(answer)
                print(i+1,j+1)
                break

for i in range(2,17):
    for j in range(19):
        if board[i][j] == 1:
            if board[i-1][j] == 1 and board[i-2][j] == 1 and board[i+1][j] == 1 and board[i+2][j] == 1:
                answer = 1
                print(answer)
                print(i+1,j+1)
                break       
        elif board[i][j] == 2:
            if board[i+1][j] == 2 and board[i+2][j] == 2 and board[i-1][j] == 2 and board[i-2][j] == 2:
                answer = 2
                print(answer)
                print(i+1,j+1)
                break  


if answer == 0:
    print(answer)