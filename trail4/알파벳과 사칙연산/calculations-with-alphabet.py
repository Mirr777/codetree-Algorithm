expression = input()

# Please write your code here.
path = []
new_path = []
def KFC(lev):
    if lev == 6:
        cal(expression,path)
        return
    for i in range(1,5):
        path.append(i)
        KFC(lev+1)
        path.pop()

max_answer = float("-inf")
def cal(expression, path):
    global max_answer
    answer = 0
    
    alpha = []
    calcul = []
    for i in expression:
        if i == "a":
            alpha.append(path[0])
        elif i == "b":
            alpha.append(path[1])
        elif i == "c":
            alpha.append(path[2])
        elif i == "d":
            alpha.append(path[3])
        elif i == "e":
            alpha.append(path[4])
        elif i == "f":
            alpha.append(path[5])
        else:
            calcul.append(i)
    answer += int(alpha[0])
    alpha.pop(0)
    while alpha:
        if calcul[0] == "+":
            answer += int(alpha[0])
            alpha.pop(0)
            calcul.pop(0)
        elif calcul[0] == "-":
            answer -= int(alpha[0])
            alpha.pop(0)
            calcul.pop(0)
        elif calcul[0] == "*":
            answer *= int(alpha[0])
            alpha.pop(0)
            calcul.pop(0)
    max_answer = max(max_answer ,answer)
    return 

KFC(0)
print(max_answer)
