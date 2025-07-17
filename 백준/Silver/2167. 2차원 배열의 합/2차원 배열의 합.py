import sys
input = sys.stdin.readline

n,m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
    
psum = [[0 for _ in range(m+1)] for _ in range(n + 1)]

for x in range(1, n+1):
    for y in range(1, m+1):
        psum[x][y] = arr[x-1][y-1] + psum[x-1][y] + psum[x][y-1] - psum[x-1][y-1]

for _ in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    total = psum[x2][y2] - psum[x1-1][y2] - psum[x2][y1 - 1] + psum[x1-1][y1-1]
    print(total)