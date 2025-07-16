def solution(n):
    answer = set([1])
    for i in range(2,n+1):
        if n % i == 0:
            answer.add(i)
    return sorted(list(answer))