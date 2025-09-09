import sys
import heapq

input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())

graph = [[] for _ in range(V+1)]
arr = [float('inf')] * (V+1)
arr[K] = 0

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

heap = []
heapq.heappush(heap, (0, K))

while heap:
    weight, node = heapq.heappop(heap)
    
    if arr[node] < weight:
        continue
    
    for curr_node, curr_weight in graph[node]:
        curr_cost = weight + curr_weight
        if curr_cost < arr[curr_node]:
            arr[curr_node] = curr_cost
            heapq.heappush(heap, (curr_cost, curr_node))

for i in range(1, V+1):
    if arr[i] == float('inf'):
        print("INF")
    else:
        print(arr[i])
