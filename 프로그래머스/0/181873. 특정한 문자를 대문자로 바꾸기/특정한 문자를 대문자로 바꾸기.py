def solution(my_string, alp):
    answer=''
    for my_str in my_string:
        if my_str.lower() == alp.lower():
            answer += my_str.upper()
        else:
            answer += my_str.lower()
    return answer