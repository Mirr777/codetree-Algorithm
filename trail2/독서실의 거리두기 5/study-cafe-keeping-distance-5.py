N = int(input())
seat = input()

# Please write your code here.
min_dis = float("inf")
max_dis = float("-inf")
for i in range(N):
    arr = []
    if seat[i] == "1": continue
    elif seat[i] == "0":
        arr.append(i)
    for idx, ele in enumerate(seat):
        if ele == "1":
            arr.append(idx)
    arr.sort()
    dis_arr = []
    for j in range(len(arr)-1):
        dis = arr[j+1] - arr[j]
        dis_arr.append(dis)
    min_dis = min(dis_arr)
    max_dis = max(min_dis,max_dis)
print(max_dis)