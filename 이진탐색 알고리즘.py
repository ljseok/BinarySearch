def binary_search(array, target, start, end): # 이진탐색 구현 함수
    if start > end: # 시작점이 끝점보다 큰경우
        return None
    mid = (start + end) // 2

    if array[mid] == target: # 찾은경우 중간점 인덱스 반환
        return mid
    elif array[mid] > target: # 중간 점 인덱스가 타깃보다 클 경우
        return binary_search(array, target, start, mid-1) # 왼쪽 값 확인
    else: # 중간 점 인덱스가 타깃보다 작을경우
        return binary_search(array, target, mid+1, end) # 오른쪽 값 확인

n, target = list(map(int,input().split()))
array = list(map(int,input().split()))

result = binary_search(array, target, 0, n-1) # 이진탐색 결과 출력
if result== None:
    print("원소가 존재하지 않습니다.")
else:
    print(result+1)

