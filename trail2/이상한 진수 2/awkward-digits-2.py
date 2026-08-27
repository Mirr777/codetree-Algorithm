a = input()

# Please write your code here.
if "0" in a:
    a= a.replace("0", "1", 1)
    print(int(a,2))
else:
    print(int(a,2)-1)