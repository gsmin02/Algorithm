import sys

input = sys.stdin.readline

N = int(input())
arrN = list(map(int, input().split()))
M = int(input())

arrN = sorted(arrN)

def calc(mid):
    curr = 0
    for ele in arrN:
        curr += min(ele, mid)
    return curr

answer = 0
if sum(arrN) < M:
    answer = arrN[-1]
else:
    start = 0
    end = arrN[-1]
    
    while start <= end:
        mid = (start + end)//2
        if calc(mid) <= M:
            answer = mid
            start = mid + 1
        else:
            end = mid - 1

print(answer)