import sys

input = sys.stdin.readline

N, East, West, North, South = map(int, input().split())

probs = [East * 0.01, West * 0.01, North * 0.01, South * 0.01]

visited = [[False] * 30 for _ in range(30)]
move = [(1,0), (-1, 0), (0, -1), (0,1)]

def canMove(x, y):
    return (0 <= x < 30) and (0 <= y < 30)
def canSolve(depth):
    return depth == N

def dfs(x, y, depth, prob):
    global result
    if canSolve(depth):
        result += prob
        return
    
    visited[x][y] = True
    for i, (dx, dy) in enumerate(move):
        nx, ny = x+dx, y+dy
        if canMove(nx, ny):
            if visited[nx][ny] == False:
                visited[nx][ny] = True
                dfs(nx, ny, depth+1, prob * probs[i])
                visited[nx][ny] = False

result = 0.0
dfs(14, 14, 0, 1)
print(result)