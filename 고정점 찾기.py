def bin(arr, st, end):
    if st > end:
        return None
    mid = (st + end) // 2

    if arr[mid] == mid:
        return mid
    elif arr[mid] > mid:
        return bin(arr, st, mid - 1)
    else:
        return bin(arr, mid + 1, end)

n = int(input())
arr = list(map(int, input().split()))

res = bin(arr, 0, n-1)

if res == None:
    print(-1)
else:
    print(res)