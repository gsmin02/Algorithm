from collections import deque
import sys

input = sys.stdin.readline
N, K = map(int, input().split())
MAX = 100001
visited = [False] * MAX
queue = deque([(N, 0)])
visited[N] = True

while queue:
    x, time = queue.popleft()
    
    if x == K:
        print(time)
        break
    
    for nx in (x-1, x+1, 2*x):
        if 0 <= nx < MAX and not visited[nx]:
            visited[nx] = True
            queue.append((nx, time + 1))