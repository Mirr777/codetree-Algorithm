n = int(input())
a = list(map(int, input().split()))

# Please write your code here.

def second(a,n):
    answer = float("inf")
    answer_idx = 0
    for idx, ele in enumerate(a):
        if ele == min(a): continue
        else:
            if ele < answer:
                answer = ele
                answer_idx = idx+1
    if a.count(answer) >1:
        return -1
    if answer == float("inf"):
        return -1
    return answer_idx
print(second(a,n))