from collections import deque
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(start):
    queue = deque([start])
    visited[start] = True
    
    while queue:
        node = queue.popleft()
        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)

count = 0
for i in range(1, N+1):
    if not visited[i]:
        bfs(i)
        count += 1

print(count)