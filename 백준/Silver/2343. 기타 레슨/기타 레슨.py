import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

start = max(arr)
end = sum(arr)

answer = 0
while start <= end:
    mid = (start + end)//2
    count = 1
    curr = 0
    for ele in arr:
        if curr + ele <= mid:
            curr += ele
        else:
            count += 1
            curr = ele
    if count <= M:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1
        
print(answer)