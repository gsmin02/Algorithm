"""
[문제]
논문의 H-index를 반환
H-index는 h번 이상 인용된 논문이 h개 이상인 경우 얻는 지표

[해석]
h-index의 최대값은 n이고, 최소는 0이다

[풀이]
논문 수 정렬 후 발행 수를 기준으로 최소 인용 논문과 h을 비교
> h의 초기값은 n
> 최소 인용 논문보다 h이 큰 경우 h-1 및 다음 순회
> 변경된 h값이 n이 큰 경우 종료 및 반환
"""
def solution(citations):
    h = len(citations)
    papers = sorted(citations)
    for i in papers:
        # Solving 1: 가장 작은 인용 수보다 h가 크면 h 감소
        if i < h:
            h -= 1
        # Solving 2: h가 작으면 해당 값이 h-index
        else:
            break
    answer = h
    return answer