import sys
import heapq

input = sys.stdin.readline

N = int(input())

heap = []
for i in range(N):
    for ele in list(map(int, input().split())):
        if len(heap) < N:
            heapq.heappush(heap, ele)
        else:
            if ele > heap[0]:
                heapq.heappushpop(heap, ele)

print(heap[0])