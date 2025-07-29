import sys

input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))

arr = sorted(arr)
num = float('inf')
res = [0, 0]

left = 0
right = N - 1
while left < right:
    val = arr[left] + arr[right]
    if abs(val) < num:
        num = abs(val)
        res = [arr[left], arr[right]]
        if val == 0:
            break
    if val < num:
        left += 1
    else:
        right -= 1

print(res[0],res[1])
