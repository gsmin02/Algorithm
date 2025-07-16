import re

def solution(my_string):
    num = re.findall(r"\d+", my_string)
    answer = [int(x) for x in num]
    return sum(answer)