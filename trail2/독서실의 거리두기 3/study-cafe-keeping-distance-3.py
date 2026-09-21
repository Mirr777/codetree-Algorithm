N = int(input())
seats = input()

# Please write your code here.

seat_pos = []
for idx,ele in enumerate(seats):
    if ele == "1":
        seat_pos.append(idx)

min_distance = float("inf")
max_distance = 0
for i in range(N):
    new_pos = seat_pos[:]
    distance = 0
    distance_list = []
    if i in seat_pos:continue
    elif i not in seat_pos:
        new_pos.append(i)
        new_pos.sort()
    for j in range(len(new_pos)-1):
        distance = new_pos[j+1] - new_pos[j]
        distance_list.append(distance)

    min_distance = min(distance_list)
    max_distance = max(min_distance,max_distance)
print(max_distance)