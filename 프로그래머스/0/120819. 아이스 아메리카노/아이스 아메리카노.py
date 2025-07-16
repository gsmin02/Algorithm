def solution(money):
    cnt = 0
    while money >= 5500:
        cnt += 1
        money -= 5500
    answer = [cnt, money]
    return answer