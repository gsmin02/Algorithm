"""
[문제]
가로, 세로 길이가 주어졌을 때, 가질 수 있는 최소 크기 구현
회전을 통해 더 작은 크기로 줄일 수 있음

[해석]
회전을 할 수 있다는 것은 값의 위치를 변경 가능

[풀이]
가로 축을 항상 더 큰 축으로 설정
기존 값과 새로운 값과 비교 후 큰 것으로 변경
"""
def solution(sizes):
    x, y = 0, 0
    
    for w, h in sizes:
        # Solving 1: 가로 축을 항상 크게
        tmp = h
        if w < h:
            h = w
            w = tmp
        
        # Solving 2: 더 큰 쪽으로 변경
        x = max(x, w)
        y = max(y, h)
    
    answer = x * y
    return answer