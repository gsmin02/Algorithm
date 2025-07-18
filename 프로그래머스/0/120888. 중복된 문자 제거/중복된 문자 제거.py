def solution(my_string):
    answer = ''
    while len(my_string) > 0:
        tmp = my_string[0]
        answer += tmp
        tmp_str = ''
        for str in my_string:
            if tmp != str:
                tmp_str += str
        my_string = tmp_str
                
    return answer