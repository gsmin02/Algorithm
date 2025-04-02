from collections import deque
import sys

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    field = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    
    for _ in range(K):
        x, y = map(int, input().split())
        field[y][x] = 1
    
    dn = [-1, 1, 0, 0]
    dm = [0, 0, -1, 1]
    
    def bfs(n, m):
        queue = deque([(n, m)])
        visited[n][m] = True
        
        while queue:
            n, m = queue.popleft()
            for i in range(4):
                nn = n + dn[i]
                nm = m + dm[i]
                if 0 <= nn < N and 0 <= nm < M and field[nn][nm] == 1 and not visited[nn][nm]:
                    visited[nn][nm] = True
                    queue.append((nn, nm))
    
    count = 0
    for i in range(N):
        for j in range(M):
            if field[i][j] == 1 and not visited[i][j]:
                bfs(i, j)
                count += 1
    
    print(count)