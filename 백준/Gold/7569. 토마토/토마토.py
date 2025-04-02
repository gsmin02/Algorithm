from collections import deque
import sys

input = sys.stdin.readline
M, N, H = map(int, input().split())
box = []
queue = deque()

for h in range(H):
    layer = []
    for n in range(N):
        row = list(map(int, input().split()))
        layer.append(row)
        for m in range(M):
            if row[m] == 1:
                queue.append((h, n, m, 0))
    box.append(layer)

dh = [-1, 1, 0, 0, 0, 0]
dn = [0, 0, -1, 1, 0, 0]
dm = [0, 0, 0, 0, -1, 1]

def bfs():
    max_days = 0
    while queue:
        h, n, m, days = queue.popleft()
        max_days = max(max_days, days)
        
        for i in range(6):
            nh = h + dh[i]
            nn = n + dn[i]
            nm = m + dm[i]
            
            if (0 <= nh < H and 0 <= nn < N and 0 <= nm < M and 
                box[nh][nn][nm] == 0):
                box[nh][nn][nm] = 1
                queue.append((nh, nn, nm, days + 1))
    
    return max_days

result = bfs()

for h in range(H):
    for n in range(N):
        for m in range(M):
            if box[h][n][m] == 0:
                print(-1)
                sys.exit(0)

print(result)

def main():
    print(">>> Sample run for Baekjoon 7569")
    print(f"Result: {result}")