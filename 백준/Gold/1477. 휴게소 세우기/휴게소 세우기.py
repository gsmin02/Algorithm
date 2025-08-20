import sys

input = sys.stdin.readline

N, M, L = map(int, input().split())
arr = list(map(int, input().split()))

arr.append(0)
arr.append(L)
arr = sorted(arr)

start = 1
end = L - 1
answer = L
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in range(1, len(arr)):
        cnt += (arr[i] - arr[i-1] - 1) // mid
        
    if cnt > M:
        start = mid + 1
    else:
        answer = mid
        end = mid - 1
        
print(answer)