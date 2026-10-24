n = int(input())

# Please write your code here.
num = []
 
def possible():
    global num
    for i in range(1,len(num)//2+1):
        for j in range(len(num)-i):
            if num[j:j+i] == num[j+i:j+i+i]:
                return False
    return True
 
def find_min(cnt):
    global num
    if cnt == n:
        ans = ''
        for j in num:
            ans = ans+str(j)
        print(ans)
        return
 
    for i in range(4,7):
        num.append(str(i))
        if possible():
            find_min(cnt+1)
            if len(num) == n:
                return
        num.pop()
 
find_min(0)