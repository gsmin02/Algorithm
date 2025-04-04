import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)
N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

start, end = map(int, input().split())
dist = [INF] * (N + 1)
dist[start] = 0

def dijk(start):
    pq = [(0, start)]
    while pq:
        current_dist, u = heapq.heappop(pq)
        
        if current_dist > dist[u]:
            continue
        
        for v, weight in graph[u]:
            cost = current_dist + weight
            if cost < dist[v]:
                dist[v] = cost
                heapq.heappush(pq, (cost, v))

dijk(start)
print(dist[end])