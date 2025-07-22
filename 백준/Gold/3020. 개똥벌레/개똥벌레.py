import sys
input = sys.stdin.readline

N, H = map(int, input().split())

diff_obj = [0] * (H)
for i in range(N):
    num = int(input())
    if i % 2 == 0:
        diff_obj[0] += 1
        diff_obj[num] -= 1
    else:
        diff_obj[H - num] += 1

min_value = float('inf')
min_range = 0

curr_obj = 0
for i in range(H):
    curr_obj += diff_obj[i]
    
    if curr_obj < min_value:
        min_value = curr_obj
        min_range = 1
    elif curr_obj == min_value:
        min_range += 1

print(min_value, min_range)