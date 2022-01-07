n,m = map(int, input().split()) # 떡의 갯수, 떡의 길이 입력
arr = list(map(int,input().split())) # 떡의 높이 입력받기

st = 0 # 시작점을 0으로 초기화
end = max(arr) # 끝점을 배열의 최대길이로 지정

result = 0
while (st <= end):
    total = 0
    mid = (st + end) // 2

    for i in arr:
        if i > mid: # 떡의 길이가 절단기 보다 클 경우에만
            total += i - mid
    if total < m: # 떡의 양이 더 부족한 경우 왼쪽 탐색
        end = mid - 1
    else: # 떡의 양이 충분한 경우 오른쪽 탐색
        result = mid
        st = mid + 1
print(result)



