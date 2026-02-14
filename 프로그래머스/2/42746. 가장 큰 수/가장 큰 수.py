"""
[문제]
0 또는 양의 정수로 만들 수 있는 가장 큰 수를 출력

[해석]
숫자의 요소를 정렬하여 가장 큰 수를 만들어야 함
단, 10인 경우 1과 0으로 쪼갤 수 없음
자릿수가 두 자리 이상인 경우 다음의 오는 자리가 다른 숫자의 자리보다 커야 함
> 30의 경우 3 다음 0 이므로 일반 3이 먼저 와야 한다
> 일반 3은 3 다음 3 이므로 30보다 먼저 온다

[풀이]
숫자를 문자열로 변경한 후 정렬 수행
정렬 시 1,000 으로 세 자리 수이기에 문자열 3배 후 정렬 수행
"""
def solution(numbers):
    # Solving 1: 숫자를 문자로 변형
    str_num = list(map(str, numbers))
    # Solving 2: 자릿수를 3배 후 정렬 수행
    answer = sorted(str_num, key= lambda x : x*3, reverse=True)
    # Solving 3: 0으로만 이루어진 경우 제외
    return str(int(''.join(answer)))