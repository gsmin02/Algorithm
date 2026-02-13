"""
[문제]
마라톤 참여 인원 배열과 완주 인원 배열이 주어졌을 때
완주하지 못한 선수를 출력
단, 참여자 중 동명이인이 있을 수 있음

[해석]
참여 선수 배열과 완주 선수 배열을 비교
완주 선수에 없는 한명의 선수를 찾아내야 함

[풀이]
파이썬 hash()의 고유 해시값(정수) 반환 특징을 활용
> 해시 변환 후 dict의 key-value로 저장
전체 해시값을 연산하여 남은 하나의 해시 추출
> 문제에서 항상 1만큼 작기에 연산으로 풀이 가능
> 참여 인원 해시는 증가, 완주 인원 해시는 감소로 풀이
"""
def solution(participant, completion):
    # Preprocess
    answer = 0
    runner = {}
    
    # Solving 1: 해시 증가
    for p in participant:
        p_hash = hash(p)
        answer += p_hash
        runner[p_hash] = p
    
    # Solving 2: 해시 감소
    for c in completion:
        c_hash = hash(c)
        answer -= c_hash
    
    # Return
    return runner[answer]