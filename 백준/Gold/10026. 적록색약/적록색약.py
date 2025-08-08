import sys
from collections import deque

sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())
graph = [sys.stdin.readline().strip() for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, visited, matrix):
    q = deque([(x, y)])
    visited[x][y] = True
    color = matrix[x][y]
    
    while q:
        curr_x, curr_y = q.popleft()
        
        for i in range(4):
            nx = curr_x + dx[i]
            ny = curr_y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and matrix[nx][ny] == color:
                visited[nx][ny] = True
                q.append((nx, ny))

visited1 = [[False] * n for _ in range(n)]
cnt1 = 0

for i in range(n):
    for j in range(n):
        if not visited1[i][j]:
            bfs(i, j, visited1, graph)
            cnt1 += 1

color_weak_graph = [row.replace('G', 'R') for row in graph]
visited2 = [[False] * n for _ in range(n)]
cnt2 = 0

for i in range(n):
    for j in range(n):
        if not visited2[i][j]:
            bfs(i, j, visited2, color_weak_graph)
            cnt2 += 1

print(cnt1, cnt2)