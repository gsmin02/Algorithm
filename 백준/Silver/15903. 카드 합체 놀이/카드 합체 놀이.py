import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
heap = []

for ele in arr:
    heapq.heappush(heap, ele)

for _ in range(m):
    first, second = heapq.heappop(heap), heapq.heappop(heap)
    num = first + second
    heapq.heappush(heap, num)
    heapq.heappush(heap, num)

print(sum(heap))