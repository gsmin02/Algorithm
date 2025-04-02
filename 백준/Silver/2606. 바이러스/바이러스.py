from collections import deque
import sys

input = sys.stdin.readline
N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque([1])
visited[1] = True
count = 0

while queue:
    node = queue.popleft()
    for next_node in graph[node]:
        if not visited[next_node]:
            visited[next_node] = True
            queue.append(next_node)
            count += 1

print(count)