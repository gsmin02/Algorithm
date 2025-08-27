import sys

input = sys.stdin.readline

C, N = map(int, input().split())
arr = [tuple(map(int, input().split())) for _ in range(N)]
dp = [float('inf')] * (C + 101)
dp[0] = 0

for c, m in arr:
    for i in range(m, C + 101):
        dp[i] = min(dp[i], dp[i-m] + c)

print(min(dp[C:]))