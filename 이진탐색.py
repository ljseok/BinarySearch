def binary_search(array, target, start, end):
    if start > end: # 끝점보다 시작점이 크다면
        return None
    mid = (start+end) // 2

    if array[mid] == target: # 찾았다면
        return mid # 중간점 반횐
    elif array[mid] > target: # 중간 점이 타깃보다 크다면
        return binary_search(array, target, start, mid - 1) # 왼쪽확인
    else:  # 중간 점이 타깃보다 작다면
        return binary_search(array, target, mid + 1 , end) # 오"른쪽 확인

n,target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않는다")
else:
    print(result+1)