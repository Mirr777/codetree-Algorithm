n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def insertion_sort(arr):
    size = len(arr)
    
    # 1번째 인덱스부터 마지막 인덱스까지 반복
    for i in range(1, size):
        key = arr[i]
        j = i - 1
        
        # key보다 큰 이전 원소들을 오른쪽으로 한 칸씩 이동
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            
        # 알맞은 위치에 key를 삽입
        arr[j + 1] = key
        
    return arr
print(*insertion_sort(arr))