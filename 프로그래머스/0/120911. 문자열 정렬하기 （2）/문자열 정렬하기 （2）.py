def solution(my_string):
    answer = ''
    for str in sorted(my_string.lower()):
        answer += str
    return answer