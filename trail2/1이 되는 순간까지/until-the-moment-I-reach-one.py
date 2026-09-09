N = int(input())

# Please write your code here.
count = 0
def one(n):
    global count
    if n == 1:
        return count
    elif n % 2 == 1:
        count += 1
        return one(n//3)
    else:
        count += 1
        return one(n//2)
print(one(N))