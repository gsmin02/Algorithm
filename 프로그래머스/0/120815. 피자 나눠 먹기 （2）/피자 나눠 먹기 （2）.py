def solution(n):
    p = 6
    c = 1
    while (n*c) % p != 0:
        c += 1
    answer = n*c/p
    return answer