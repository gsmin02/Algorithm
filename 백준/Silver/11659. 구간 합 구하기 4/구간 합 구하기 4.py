import sys
input = sys.stdin.readline

n,m = map(int, input().split())

arr_n = list(map(int, input().split(" ")))

psum = [0] * (n+1)
for i in range(1, n+1):
    psum[i] += psum[i-1] + arr_n[i-1]
    
for _ in range(m):
    i, j = map(int, input().split())
    print(str(psum[j]-psum[i-1]))
