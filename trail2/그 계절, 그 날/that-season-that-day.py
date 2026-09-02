Y, M, D = map(int, input().split())

# Please write your code here.
def season(Y,M,D):
    if Y % 4 == 0 and Y % 100 != 0:
        if M == 2:
            if D >=30:
                return -1
        elif M == 2 or M == 4 or M == 6 or  M == 9 or M == 11:
            if D >= 31:
                return -1
    elif Y % 400 == 0:
        if M == 2:
            if D >=30:
                return -1
        elif M == 2 or M == 4 or M == 6 or  M == 9 or M == 11:
            if D >= 31:
                return -1
    
    else:
        if M ==2:
            if D >=29:
                return -1
        elif M == 2 or M == 4 or M == 6 or  M == 9 or M == 11:
            if D >= 31 :
                return -1
    if 3 <= M <= 5:
        return "Spring"
    elif 6<= M <= 8:
        return "Summer"
    elif 9 <= M <= 11:
        return "Fall"
    elif M == 12 or M <=2:
        return "Winter"
print(season(Y, M, D))