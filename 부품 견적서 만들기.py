def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

n = int(input()) # 매장의 부품 갯수 입력
array = list(map(int, input().split()))
array.sort()

m = int(input()) # 손님이 문의한 부품의 갯수
x = list(map(int,input().split())) # 손님이 확인한 부품

for i in x:
    result = binary_search(array, i, 0, n-1)

    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')