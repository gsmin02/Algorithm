def solution(num, k):
    str = []
    answer = -1
    while num > 0:
        str.insert(0, num % 10)
        num = num // 10
    for i in range(len(str)):
        if str[i] == k:
            answer = i+1
            break
    return answer