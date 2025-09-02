import sys

input = sys.stdin.readline

N = int(input())
K = int(input())
arr = list(map(int, input().split()))

answer = 0
if N <= K:
    print(answer)
else:
    arr.sort()
    dist = []
    for i in range(1, N):
        dist.append(arr[i] - arr[i-1])

    dist.sort()
    answer = sum(dist[:N-K])

    print(answer)