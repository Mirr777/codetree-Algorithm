a, b, x, y = map(int, input().split())

# Please write your code here.
def tele(a,b,x,y):
    A = abs(b-a)
    B = abs(x-a) + abs(y-b)
    C = abs(a-y) + abs(b-x)
    answer = min(A,B,C)
    return answer
print(tele(a,b,x,y))