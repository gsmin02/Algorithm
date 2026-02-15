"""
[문제]
주어진 패턴이 존재할 때, 입력 패턴과 가장 동일한 번호를 출력

[해석]
학생들의 패턴을 정답과 비교
각각 패턴이 다르기 때문에 동일한 구간을 비교

[풀이]
패턴 저장 후 % 연산을 통해 동일한 지점 추출 후 비교
최고점을 찾은 후 최고점과 동일하게 맞춘 경우 결과에 추가
"""
def solution(answers):
    answer = []
    
    st_1 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    hit_1 = 0
    st_2 = [2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5]
    hit_2 = 0
    st_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    hit_3 = 0
    
    for i in range(len(answers)):
        # Solving 1: % 연산을 통한 패턴 적용
        if st_1[i%len(st_1)] == answers[i]:
            hit_1 += 1
        if st_2[i%len(st_2)] == answers[i]:
            hit_2 += 1
        if st_3[i%len(st_3)] == answers[i]:
            hit_3 += 1
    
    # Solving 2: 최대값 추출 후 append
    max_score = max(hit_1, hit_2, hit_3)
    if max_score==hit_1:
        answer.append(1)
    if max_score==hit_2:
        answer.append(2)
    if max_score==hit_3:
        answer.append(3)
    
    return answer