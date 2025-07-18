def solution(myString):
    answer = ''
    for my_str in myString:
        if my_str < 'l':
            answer += 'l'
        else:
            answer += my_str
    return answer