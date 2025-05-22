import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
schools = [0] * 2000001

for i in arr:
    schools[i] += 1

res = 0
for i in range(1, 2000001):
    cnt = 0
    for j in range(i, 2000001, i):
        cnt += schools[j]
    if cnt >= 2:
        res = max(res, cnt * i)

print(res)