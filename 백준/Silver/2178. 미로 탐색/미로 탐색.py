from collections import deque
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
queue = deque([(0, 0, 1)])
visited[0][0] = True

dn = [-1, 1, 0, 0]
dm = [0, 0, -1, 1]

while queue:
    n, m, dist = queue.popleft()
    
    if n == N-1 and m == M-1:
        print(dist)
        break
    
    for i in range(4):
        nn = n + dn[i]
        nm = m + dm[i]
        
        if 0 <= nn < N and 0 <= nm < M and maze[nn][nm] == 1 and not visited[nn][nm]:
            visited[nn][nm] = True
            queue.append((nn, nm, dist + 1))