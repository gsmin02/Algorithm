import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
def bfs(x, y, visited):
    q = deque()
    q.append((x,y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M: continue
            if visited[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append((nx, ny))

walls = []
virus = []
for x in range(N):
    for y in range(M):
        if graph[x][y] == 0: walls.append([x, y])
        elif graph[x][y] == 2: virus.append([x, y])

result = 0
l = len(walls)
for i in range(l):
    for j in range(i + 1, l):
        for k in range(j + 1, l):
            cnt = 0
            visited = [[0 if graph[x][y] == 0 else 1 for y in range(M)] for x in range(N)]
            
            visited[walls[i][0]][walls[i][1]] = 9
            visited[walls[j][0]][walls[j][1]] = 9
            visited[walls[k][0]][walls[k][1]] = 9
            
            for v in virus:
                bfs(v[0], v[1], visited=visited)
                
            for x in range(N):
                for y in range(M):
                    if visited[x][y] == 0:
                        cnt += 1
            result = max(result, cnt)
print(result)