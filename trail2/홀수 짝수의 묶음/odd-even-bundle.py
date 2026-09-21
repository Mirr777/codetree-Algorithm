N = int(input())
numbers = list(map(int, input().split()))

# Please write your code here.
even_number = 0
odd_number = 0
for i in range(N):
    if numbers[i] % 2 == 0:
        even_number += 1
    else:
        odd_number += 1


if even_number > odd_number:
    print(odd_number*2 +1)
elif even_number == odd_number:
    print(odd_number*2)
else:
    if (odd_number - even_number) % 3 == 1: 
        print(even_number*2 + (odd_number - even_number)//3 *2 -1)
    elif (odd_number - even_number) % 3 == 2:
        print(even_number*2 + (odd_number - even_number)//3 *2 +1)
    elif (odd_number - even_number) % 3 == 0:
        print(even_number*2 + (odd_number - even_number)//3  * 2)
