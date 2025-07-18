def solution(numbers):
    s = sorted(numbers, reverse=True)
    answer = s[0] * s[1]
    return answer