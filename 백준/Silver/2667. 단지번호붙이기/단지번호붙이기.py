from collections import deque
import sys

input = sys.stdin.readline
N = int(input())
grid = [list(map(int, input().strip())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
dn = [-1, 1, 0, 0]
dm = [0, 0, -1, 1]
complexes = []

def bfs(n, m):
    queue = deque([(n, m)])
    visited[n][m] = True
    count = 1
    
    while queue:
        n, m = queue.popleft()
        for i in range(4):
            nn = n + dn[i]
            nm = m + dm[i]
            if 0 <= nn < N and 0 <= nm < N and grid[nn][nm] == 1 and not visited[nn][nm]:
                visited[nn][nm] = True
                queue.append((nn, nm))
                count += 1
    return count

for i in range(N):
    for j in range(N):
        if grid[i][j] == 1 and not visited[i][j]:
            complexes.append(bfs(i, j))

print(len(complexes))
for size in sorted(complexes):
    print(size)