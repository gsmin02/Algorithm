def solution(n):
    f = 1
    answer = 0
    for i in range(1,11):
        f *= i
        if f == n:
            answer = i
            break
        elif f > n:
            answer = i - 1
            break
    return answer