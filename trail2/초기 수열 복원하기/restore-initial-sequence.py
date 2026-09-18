n = int(input())
adjacent = list(map(int, input().split())) if n >= 2 else []

# Please write your code here.
def suyeol(arr,n):
    if n ==1 :
        return [n]
    for i in range(1, 1000):
        adjacent_list = []
        a = i
        adjacent_list.append(a)
        for j in arr:
            b = j - a
            if a == b or b<=0:continue
            else:
                a = b
                adjacent_list.append(a)
            if len(adjacent_list) ==n and len(adjacent_list) == len(set(adjacent_list)):
                return adjacent_list
print(*suyeol(adjacent,n))