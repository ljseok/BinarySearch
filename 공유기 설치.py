n,c = map(int, input().split()) # 집의 갯수와 공유기의 갯수 입력받기
arr = []

for _ in range(n):
    arr.append(int(input()))
arr.sort()

st = 1 # 최소거리 1 초기화
end = arr[-1] - arr[0] # 최대거리
dist = 0

while(st<=end):
    mid = (st+end) // 2 # 인접한 공유기 2개의 거리
    val = arr[0] # 배열의 가장 아래
    cnt = 1

    for i in range(1,n): # 공유기 설치
        if arr[i] >= val + mid:
            val = arr[i]
            cnt += 1

    if cnt>=c: # c개 이상의 공유기를 설치할 수 있으면
        st = mid + 1 # 거리를 증가
        dist = mid
    else: # 공유기를 설치할 수 없으면
        end = mid - 1 # 거리를 감소
print(dist)

