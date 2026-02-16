"""
[문제]
최초 상태와 접근 가능 조건, 소모량이 주어졌을 때, 최대로 많이 탐색할 수 있는 방법 탐색

[해석]
각 상태를 유지하면서 순회 조건을 달성해야 함
permutations() 활용 모든 조건 추출 후 비교

[풀이]
순회 가능한 모든 조합을 추출
해당 순열로 조건부 탐색
최대 깊이 도달한 경우 최신화하여 최종 반환
"""
from itertools import permutations

def solution(k, dungeons):
    answer = 0
    
    # Solving 1: 길이에 따른 순열 추출
    for p in permutations(dungeons, len(dungeons)):
        # Solving 2: 지역적으로 초기 조건값 설정
        tmp_k = k
        depth = 0
        
        for condition, amount in p:
            # Solving 3: 접근 가능한 경우 연산
            if tmp_k >= condition:
                tmp_k -= amount
                depth += 1
            # Solving 4: 최대값 업데이트
            answer = max(depth, answer)
    
    return answer