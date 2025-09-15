import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N)]
topology = [0] * N

for i in range(M):
    X, Y, K = map(int, input().split())
    graph[X-1].append((Y-1, K))
    topology[Y-1] += 1

answer = [0] * N
answer[N-1] = 1

queue = deque()
queue.append(N-1)

while queue:
    curr = queue.popleft()
    
    for y, k in graph[curr]:
        answer[y] += k * answer[curr]
        topology[y] -= 1
        
        if topology[y] == 0:
            queue.append(y)

for i in range(N):
    if len(graph[i]) == 0:
        print(i+1, answer[i])