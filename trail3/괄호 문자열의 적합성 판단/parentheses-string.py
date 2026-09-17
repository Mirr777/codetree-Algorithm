str = input()

# Please write your code here.
stack = []
def stack_find(str):
    for i in str:
        if stack:
            if stack[-1] == "(" and i == ")":
                stack.pop()
            elif stack[-1] == ")" and i == ")":
                return "No"
            else:
                stack.append(i)
        else:
            stack.append(i)
    if stack == []:
        return "Yes"
    else:
        return "No"
print(stack_find(str))