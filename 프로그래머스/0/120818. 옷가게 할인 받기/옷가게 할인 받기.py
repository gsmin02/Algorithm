def solution(price):
    if price >= 500000:
        price -= price / 5
    elif price >= 300000:
        price -= price / 10
    elif price >= 100000:
        price -= price / 20
    answer = int(price)
    return answer