def solution(s):
    answer = [0, 0]
    s = "0b"+s
    while s[2:] != "1":
        answer[0] += 1
        answer[1] += s[2:].count("0")
        s = str(bin(s[2:].count("1")))
    return answer