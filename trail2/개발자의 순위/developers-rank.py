k, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(k)]

# Please write your code here.
arr_list = []
answer = 0
for j in range(1,n+1):    
    arr_list = []
    for i in range(k):
        
        a = arr[i].index(j)
        for m in range(a+1, n):
            arr_list.append(arr[i][m])
    for l in range(1,n+1):
        b = arr_list.count(l)
        if b == k:
            answer +=1
print(answer)