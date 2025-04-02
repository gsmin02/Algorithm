from collections import deque
import sys

input = sys.stdin.readline
M, N = map(int, input().split())
box = []
queue = deque()

for n in range(N):
    row = list(map(int, input().split()))
    box.append(row)
    for m in range(M):
        if row[m] == 1:
            queue.append((n, m, 0))

dn = [-1, 1, 0, 0]
dm = [0, 0, -1, 1]

def bfs():
    max_days = 0
    while queue:
        n, m, days = queue.popleft()
        max_days = max(max_days, days)
        
        for i in range(4):
            nn = n + dn[i]
            nm = m + dm[i]
            
            if 0 <= nn < N and 0 <= nm < M and box[nn][nm] == 0:
                box[nn][nm] = 1
                queue.append((nn, nm, days + 1))
    
    return max_days

result = bfs()

for n in range(N):
    for m in range(M):
        if box[n][m] == 0:
            print(-1)
            sys.exit(0)

print(result)