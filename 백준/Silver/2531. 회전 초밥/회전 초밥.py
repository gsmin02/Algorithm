import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
arr = [int(input()) for _ in range(N)]

ans = -1
dish = [0] * (d + 1)
dish[c] = 1
count = 1

for i in range(k):
    if dish[arr[i]] == 0:
        count += 1
    dish[arr[i]] += 1

ans = count
for i in range(N):
    j = (i + k) % N
    if dish[arr[j]] == 0:
        count += 1
    dish[arr[j]] += 1
    if dish[arr[i]] == 1:
        count -= 1
    dish[arr[i]] -= 1
    ans = max(ans, count)

print(ans)