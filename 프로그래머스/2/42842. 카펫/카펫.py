"""
[문제]
중심 사각형의 넓이만 주어였을 때
한겹 더 두른 둘레의 크기와 동일한 값의 가로, 세로 크기 반환

[해석]
전체 사각형의 넓이는 brown+yellow
두른 사각형의 가로세로 합은 (brown+4)/2

[풀이]
전체 사각형의 넓이를 소인수 분해
그 합이 가로세로 합과 동일한 값을 탐색
"""
def factorization(num):
    result = []
    for i in range(2, num//2+1):
        if num % i == 0 and i <= num // i:
            result.append((num//i, i))
    return result

def solution(brown, yellow):
    answer = []
    
    total_size = brown+yellow
    sum_wh = (brown+4)/2
    
    for w, h in factorization(total_size):
        if w+h == sum_wh:
            answer = [w, h]
    
    return answer