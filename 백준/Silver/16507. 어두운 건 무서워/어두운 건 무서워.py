import sys
input = sys.stdin.readline

R, C, Q = map(int, input().split())

pic = [list(map(int, input().split())) for _ in range(R)]

psum = [[0] * (C + 1) for _ in range(R + 1)]
for i in range(1, R + 1):
    for j in range(1, C + 1):
        psum[i][j] = pic[i-1][j-1] + psum[i-1][j] + psum[i][j-1] - psum[i-1][j-1]

def range_mean(x1, y1, x2, y2):
    sum = psum[x2][y2] - psum[x2][y1-1] - psum[x1-1][y2] + psum[x1-1][y1-1]
    size = (x2 - x1 + 1) * (y2 - y1 + 1)
    return sum // size

answer = ""
for _ in range(Q):
    x1, y1, x2, y2 = map(int, input().split())
    answer += str(range_mean(x1, y1, x2, y2)) + "\n"

print(answer)