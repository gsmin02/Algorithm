def solution(age):
    a = ["a","b","c","d","e","f","g","h","i","j"]
    answer = ''
    while age > 0:
        answer = a[age % 10] + answer
        age = age // 10
    return answer