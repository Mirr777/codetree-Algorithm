N = int(input())
str = input()

# Please write your code here.
def length(N,str):
    for i in range(N):
        alp_list = set()
        for j in range(N-i):
            alp = ""
            for k in range(j,j+i+1):
                alp += str[k]
            alp_list.add(alp)
        if len(alp_list) == N-i:
            return i+1
print(length(N,str))