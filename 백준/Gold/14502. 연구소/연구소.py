from collections import deque
import copy

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def virus(x, y, temp):
    queue = deque([(x, y)])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and temp[nx][ny] == 0:
                temp[nx][ny] = 2
                queue.append((nx, ny))

def get_safe_area(temp):
    return sum(row.count(0) for row in temp)

def wall(count):
    global max_safe
    if count == 3:
        temp = copy.deepcopy(graph)
        for i in range(N):
            for j in range(M):
                if temp[i][j] == 2:
                    virus(i, j, temp)
        max_safe = max(max_safe, get_safe_area(temp))
        return
    
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                graph[i][j] = 1
                wall(count + 1)
                graph[i][j] = 0

max_safe = 0
wall(0)
print(max_safe)