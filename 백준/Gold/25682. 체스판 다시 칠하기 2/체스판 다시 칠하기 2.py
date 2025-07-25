import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())

arr = [input().strip() for _ in range(N)]

psum_BW = [[0] * (M+1) for _ in range(N+1)]
psum_WB = [[0] * (M+1) for _ in range(N+1)]

for i in range(N):
    for j in range(M):
        chk = ((i + j) % 2 == 0)
        
        chk_w = 0
        if (chk and arr[i][j] == 'W') or (not chk and arr[i][j] == 'B'):
            chk_w = 1
        chk_b = 0
        if (not chk and arr[i][j] == 'W') or (chk and arr[i][j] == 'B'):
            chk_b = 1
        psum_BW[i+1][j+1] = chk_b + psum_BW[i][j+1] + psum_BW[i+1][j] - psum_BW[i][j]
        psum_WB[i+1][j+1] = chk_w + psum_WB[i][j+1] + psum_WB[i+1][j] - psum_WB[i][j]

min_val = float('inf')

for i in range(1, N-K+2):
    for j in range(1, M-K+2):
        r = i + K - 1
        c = j + K - 1
        
        cnt_b = psum_BW[r][c] - psum_BW[i-1][c] - psum_BW[r][j-1] + psum_BW[i-1][j-1]
        cnt_w = psum_WB[r][c] - psum_WB[i-1][c] - psum_WB[r][j-1] + psum_WB[i-1][j-1]
        
        min_val = min(min_val, cnt_b, cnt_w)

print(min_val)