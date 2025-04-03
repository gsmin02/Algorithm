from collections import deque

N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [0] * (N+1)

def bfs(start):
    queue = deque([start])
    parent[start] = start

    while queue:
        current = queue.popleft()
        for next_node in graph[current]:
            if parent[next_node] == 0:
                parent[next_node] = current
                queue.append(next_node)

bfs(1)

for i in range(2, N+1):
    print(parent[i])