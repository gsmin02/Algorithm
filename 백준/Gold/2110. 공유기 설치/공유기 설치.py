import sys

input = sys.stdin.readline

N, C = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))
arr = sorted(arr)
if C == 2:
    print(arr[-1] - arr[0])
else:
    start, end = 1, arr[-1] - arr[0]
    while start <= end:
        cnt = 1
        mid = (start + end) // 2
        curr = arr[0]
        for i in range(1, len(arr)):
            if arr[i] - curr >= mid:
                curr = arr[i]
                cnt += 1
                
        if cnt < C:
            end = mid - 1
        else:
            result = mid
            start = mid + 1
    print(result)