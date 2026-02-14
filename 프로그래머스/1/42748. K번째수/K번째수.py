"""
[문제]
i부터 j까지의 수를 뽑아 정렬 시 k번째에 있는 수를 반환

[해석]
구간 추출 후 정렬을 수행해야 함

[풀이]
반복문으로 조건 추출 후 연산
"""
def solution(array, commands):
    answer = []
    
    for i, j, k in commands:
        if i==j:
            answer.append(array[i-1])
        else:
            answer.append(sorted(array[i-1:j])[k-1])
    
    return answer