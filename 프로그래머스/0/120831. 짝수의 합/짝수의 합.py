def solution(n):
    even = n/2 if n%2 == 0 else (n-1)/2
    answer = (even*2 + 2) * even/2
    return answer