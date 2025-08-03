import sys

input = sys.stdin.readline

N, X = map(int, input().split())
view = list(map(int, input().split()))

value = sum(view[:X])
max_value = value
max_cnt = 1

for i in range(X, N):
    value += view[i]
    value -= view[i-X]

    if value > max_value:
        max_value = value
        max_cnt = 1 
    elif value == max_value:
        max_cnt += 1
        
if max(view) == 0:
    print('SAD')
else:
    print(max_value)
    print(max_cnt)