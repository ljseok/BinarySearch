from bisect import bisect_left, bisect_right

def count_by_range(a, left, right):
    right_value = bisect_right(a, right)
    left_value = bisect_left(a, left)
    return right_value - left_value

n,m = map(int, input().split()) # 데이터 갯수 , 기준점 입력
arr = list(map(int, input().split())) # 전체 데이터 입력

cnt = count_by_range(arr, m , m)

if cnt == 0:
    print(-1)
else:
    print(cnt)
