n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
arr_list = 0
max_arr = 0
for i in range(n-k+1):
    arr_list = 0
    for j in range(k):
        arr_list += arr[i+j]
    max_arr = max(max_arr, arr_list)
print(max_arr)