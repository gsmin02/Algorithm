def solution(s):
    answer = ''
    arr = {}
    
    for c in s:
        arr[c] = arr.get(c, 0) + 1
    
    for c in s:
        if arr[c] == 1:
            answer += c
    
    return ''.join(sorted(answer))