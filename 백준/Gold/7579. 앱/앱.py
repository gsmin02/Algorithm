import sys

N, M = map(int, sys.stdin.readline().split())

mem = list(map(int, sys.stdin.readline().split()))
cost = list(map(int, sys.stdin.readline().split()))

max_cost = sum(cost)
dp = [0] * (max_cost + 1)
for i in range(N):
    for j in range(max_cost, cost[i] - 1, -1):
        dp[j] = max(dp[j], dp[j - cost[i]] + mem[i])

for i in range(max_cost + 1):
    if dp[i] >= M:
        print(i)
        break