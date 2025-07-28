import sys

input = sys.stdin.readline

N, K = map(int, input().split())

psum = [0 for _ in range(N+1)]
arr = list(map(int, input().split()))
for i in range(N):
    psum[i+1] = psum[i] + arr[i]

res = psum[K]
for i in range(K+1, N+1):
    num = psum[i] - psum[i-K]
    res = max(res, num)
print(res)