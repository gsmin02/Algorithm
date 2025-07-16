def solution(n):
    answer = int(n/7)+1 if n % 7 != 0 else int(n/7)
    return answer