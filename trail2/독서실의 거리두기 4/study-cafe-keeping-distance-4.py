N = int(input())
seat = input()

# Please write your code here.
seat_point = []
for i in range(N):
    if seat[i] == "1":
        seat_point.append(i)

max_distance = 0
for j in range(N):
    for k in range(j+1,N):
        old_seat_point = seat_point[:]
        
        if j in old_seat_point or k in old_seat_point: continue
        old_seat_point.append(j)
        old_seat_point.append(k)
        
        old_seat_point.sort()
        min_distance = float("inf")
        for l in range(len(old_seat_point)-1):
            distance = old_seat_point[l+1] - old_seat_point[l]
            min_distance = min(min_distance, distance)
        max_distance = max(max_distance, min_distance)
print(max_distance)