def binary_search(array, target, start, end): # 이진탐색 함수
    while start <= end:
        mid = (start+end) //2

        if array[mid] ==target:
            return mid
        elif array[mid] > target: # 중간값이 타깃보다 큰 경우
            end = mid - 1 # 왼쪽 값 확인
        else: # 중간값이 타깃보다 작은 경우
            start = mid+1 # 오른쪽 값 확인
        return None

'''

n = int(input()) # 가게의 부품 갯수

array=list(map(int, input().split()))
array.sort()

m = int(input()) # 손님의 부품갯수 입력

x = list(map(int, input().split())) # 손님이 요청한 부품번호를 공백으로 입력
'''

n = 5
array = [8, 3, 7, 9, 2]
array.sort()
m = 3
x = [5, 7, 9]

for i in x : # 손님이 요청한 부품 확인
    result = binary_search(array, i, 0, n-1) # 부품이 존재하는지 확인

    if result != None:
        print('Yes', end=' ')
    else:
        print('No', end=' ')


