import re

def solution(s):
    arr = re.findall(r"\S+|\s+", s)
    answer = []
    for word in arr:
        if word.isspace():
            answer.append(word)
        else:
            answer.append(word[0].upper() + word[1:].lower())
        
    return "".join(answer)