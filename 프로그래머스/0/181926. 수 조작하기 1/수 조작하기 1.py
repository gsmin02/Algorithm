def solution(n, control):
    answer = n
    for i in range(len(control)):
        str = control[i]
        if str == "w":
            answer += 1
        elif str == "s":
            answer -= 1
        elif str == "d":
            answer += 10
        elif str == "a":
            answer -= 10
    return answer