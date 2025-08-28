import sys
import heapq

input = sys.stdin.readline

N = int(input())
heap = []
for _ in range(N):
    m = int(input())
    heapq.heappush(heap, m)

answer = 0
while len(heap) != 1:
    first, second = heapq.heappop(heap), heapq.heappop(heap)
    num = first + second
    answer += num
    heapq.heappush(heap, num)

print(answer)