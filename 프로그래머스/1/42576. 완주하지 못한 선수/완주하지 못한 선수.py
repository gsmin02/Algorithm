def solution(participant, completion):
    arr_p = sorted(participant)
    arr_c = sorted(completion)
    arr_c.append("")
    for i in range(len(participant)):
        if arr_p[i] != arr_c[i]:
            return arr_p[i]