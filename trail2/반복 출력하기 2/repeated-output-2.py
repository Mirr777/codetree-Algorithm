n = int(input())

# Please write your code here.
def Hello(n):
    if n == 0:
        return
    else:
        n = n -1
        print("HelloWorld")
        Hello(n)
Hello(n)