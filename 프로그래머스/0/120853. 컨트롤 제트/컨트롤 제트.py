def solution(s):
    answer = 0
    arr = s.split()
    for i in range(len(arr)):
        if arr[i] == "Z":
            arr[i-1:i+1] = [0, 0]
        else:
            arr[i] = int(arr[i])
    return sum(arr)