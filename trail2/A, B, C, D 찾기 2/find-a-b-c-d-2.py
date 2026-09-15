nums = list(map(int, input().split()))

# Please write your code here.
nums.sort()
A = nums[0]
B = nums[1]
if nums[2] == A + B:
    C = nums[3]
else:
    C = nums[2]
nums.remove(A)
nums.remove(B)
nums.remove(C)
nums.remove(A+B)
nums.remove(A+C)
nums.remove(B+C)
nums.remove(A+B+C)
D = nums[0]
print(A, B, C, D)