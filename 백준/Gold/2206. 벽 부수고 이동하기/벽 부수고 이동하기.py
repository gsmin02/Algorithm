import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().rstrip())))

visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
move = [(-1, 0), (1,0), (0, -1), (0,1)]

def canMove(x, y):
    return (0 <= x < N) and (0 <= y < M)
def canSolve(x,  y):
    return (x == N-1) and (y == M-1)

queue = deque()
queue.append([0, 0, 0])
visited[0][0][0] = 1

answer = -1
while queue:
    x, y, z = queue.popleft()
    
    if canSolve(x, y):
        answer = visited[x][y][z]
        break
    
    for dx, dy in move:
        nx, ny = x+dx, y+dy
        if canMove(nx, ny):
            if graph[nx][ny] == 0:
                if visited[nx][ny][z] == 0:
                    visited[nx][ny][z] = visited[x][y][z] + 1
                    queue.append([nx, ny, z])
            elif graph[nx][ny] == 1:
                if z == 0:
                    visited[nx][ny][z+1] = visited[x][y][z] + 1
                    queue.append([nx, ny, z+1])

print(answer)