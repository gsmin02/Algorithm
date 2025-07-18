def solution(my_string):
    num = ["0","1","2","3","4","5","6","7","8","9"]
    arr = []
    for str in my_string:
        if str in num:
            arr.append(int(str))
    answer = sorted(arr)
    return answer