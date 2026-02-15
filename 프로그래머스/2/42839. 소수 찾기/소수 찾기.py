"""
[문제]
개별로 조합가능한 숫자가 주어졌을 때, 만들 수 있는 소수의 수를 출력

[해석]
각 조각을 조합하여 소수를 구성해야 함
조합된 숫자가 소수인지 판별해야 함

[풀이]
처음 0이 오는 경우를 처리하기 위해 정수형 변환
permutations() 활용 가능한 순열 계산
소수 판별 함수로 생성된 조합과 비교
"""
import math
from itertools import permutations

# Solving 1: 소수 판별 함수 정의
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    result = set()
    number = list(map(int, numbers))
    
    # Solving 2: 순열 계산 후 저장
    for i in range(1, len(number) + 1):
        # Solving 2-1: 자릿수별 생성가능한 순열 추출
        for p in permutations(number, i):
            # Solving 2-2: 튜플을 문자열 변환 후 붙이고 정수형 변환 후 set에 추가
            result.add(int("".join(map(str, p))))
    
    # Solving 3: 소수 판별
    for num in list(result):
        if is_prime(num):
            answer += 1
            
    return answer