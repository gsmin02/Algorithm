import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
topology = [0] * (N+1)

for _ in range(M):
    p, q, r = map(int, input().split())
    graph[p].append((q, r))
    topology[q] += 1

dp = [0] * (N+1)
path = [-1] * (N+1)

queue = deque()
queue.append(1)

while queue:
    curr = queue.popleft()
    
    for q, r in graph[curr]:
        if dp[q] < dp[curr] + r:
            dp[q] = dp[curr] + r
            path[q] = curr
        
        if q == 1:
            continue
        
        topology[q] -= 1
        if topology[q] == 0:
            queue.append(q)

print(dp[1])

result = []
curr_node = path[1]
while curr_node != 1:
    result.append(curr_node)
    curr_node = path[curr_node]

result.append(1)
result.reverse()
result.append(1)
print(" ".join(map(str, result)))