from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
MAX = 100001

dist = [-1] * MAX
q = deque([N])
dist[N] = 0

while q:
    x = q.popleft()
    if x == K:
        print(dist[x])
        break
    if 0 <= x * 2 < MAX and dist[x * 2] == -1:
        dist[x * 2] = dist[x]
        q.appendleft(x * 2)
    for nx in (x - 1, x + 1):
        if 0 <= nx < MAX and dist[nx] == -1:
            dist[nx] = dist[x] + 1
            q.append(nx)