import sys
input = sys.stdin.readline

N = int(input())

num = list(map(int, input().split()))
psum = sum(num)
result = 0

for i in range(N-1):
    psum -= num[i]
    result += psum * num[i]

print(result)