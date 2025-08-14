import sys

input = sys.stdin.readline

K, N = map(int, input().split())
arr = []
for _ in range(K):
    arr.append(int(input()))

ans = 0
start, end = 0, max(arr)
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for ele in arr:
        if mid == 0:
            cnt += ele
        else:
            cnt += ele // mid
    if cnt < N:
        end = mid - 1
    else:
        ans = mid
        start = mid + 1
print(ans)