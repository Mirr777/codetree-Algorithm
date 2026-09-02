N = int(input())
a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

# Please write your code here.
answer = 0
if a1 >= N-2:
    a1 = a1 - N
if a2 >= N-2:
    a2 = a2 - N
if b1 >= N-2:
    b1 = b1 - N
if b2 >= N-2:
    b2 = b2 - N
if c1 >= N-2:
    c1 = c1 - N
if c2 >= N-2:
    c2 = c2 - N

if N >= 5:

    if abs(a1-a2) <=4 and abs(b1-b2) <=4 and abs(c1-c2) <=4:
        answer = (5 - abs(a1-a2)) * (5 - abs(b1-b2)) * (5 - abs(c1-c2)) 
    print(250-answer)

elif N < 5:
    print((N*N*N))