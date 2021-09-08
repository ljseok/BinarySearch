'''
n,m = list(map(int,input().split(' '))) # 떡의 갯수와 떡의 길이 입력받기

array= list(map(int,input().split())) # 떡의 높이 입력받기

start = 0; # 시작점
end = max(array) # 끝점
'''

n=4
m=6
array=[19, 15, 10, 17]
start=0
end=max(array)

result = 0
while(start<=end):
    total = 0
    mid = (start+end) // 2

    for x in array:
        if x > mid: # 떡이 잘렸을때
            total += x - mid

    if total < m: # 떡의 양이 모자를 때 (이진탐색에서 왼쪽 값 탐색 )
        end = mid - 1
    else: # 떡의 양이 충분할 때 (이진탐색에서 오른쪽 값 탐색)
        result = mid
        start = mid + 1

print(result)


