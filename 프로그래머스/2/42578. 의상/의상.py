"""
[문제]
의상의 종류 n개와 각 종류에 해당하는 의상이 m개 주어졌을 때, 선택 가능한 경우의 수 반환
단, 아무것도 선택하지 않는 경우의 수는 없으며, 선택되지 않는 종류가 있어도 됨

[해석]
경우의 수를 구하는 문제로 (m_i+1 * n)-1로 풀이
m_i+1: 의상 중 하나가 선택되는 경우의 수(m_i)와 선택되지 않는 경우의 수(+1)
n : 종류의 수
-1 : 전체가 선택되지 않는 경우의 수 제외

[풀이]
리스트 순회로 풀이 시 시간 초과 발생 가능
딕셔너리를 통해 바로 값을 찾아서 계산
"""
def solution(clothes):
    dic = {}
    answer = 1
    
    # Solving 1: 입력에서 종류 갯수만 추출
    for _, c in clothes:
        if c not in dic:
            dic[c] = 0
        dic[c] += 1
    
    # Solving 2: 경우의 수 계산
    for i in dic.values():
        answer *= (i + 1)
    
    # Solving 3: 선택 안하는 경우 제외
    return answer - 1