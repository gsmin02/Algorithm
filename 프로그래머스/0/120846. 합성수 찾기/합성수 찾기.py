def div(n):
    return list(filter(lambda v: n % v == 0, range(1, n+1)))

def solution(n):
    return len(list(filter(lambda v: len(div(v)) >= 3, range(1, n+1))))