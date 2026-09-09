n = int(input())

# Please write your code here.
def rule(N):
    if N == 0:
        return
    print(n-N+1, end = " ")
    rule(N-1)

def inverse_rule(N):
    if N == 0:
        return
    print(N, end = " ")
    inverse_rule(N-1)

rule(n)
print()
inverse_rule(n)