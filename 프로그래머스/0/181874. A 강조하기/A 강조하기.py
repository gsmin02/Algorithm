def solution(myString):
    answer = ''
    for my_str in myString:
        if my_str.lower() == "a":
            answer += my_str.upper()
        else:
            answer += my_str.lower()
    return answer