def solution(myString, pat):
    my_str = ''.join(["B" if c == "A" else "A" for c in pat])
    return 1 if my_str in myString else 0