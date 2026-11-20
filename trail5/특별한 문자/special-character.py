str = input()

# Please write your code here.
d = dict()
answer = dict()
for i in str:
    if i not in d:
        d[i] = 1
        answer[i] = 1
    else:
        d[i] += 1
        if i in answer:
            answer.pop(i)

if answer == {}:
    print(None)
else:
    for k, v in answer.items():
        print(k)
        break