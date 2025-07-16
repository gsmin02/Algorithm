def rep(i, j):
    cnt = 0
    while i > 0:
        if i % 10 == j:
            cnt += 1
        i = i // 10
    return cnt

def solution(i, j, k):
    answer = 0
    for n in range(i, j+1):
        answer += rep(n, k)
    return answer