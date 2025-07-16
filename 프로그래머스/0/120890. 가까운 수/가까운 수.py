def solution(array, n):
    arr = [(abs(n - x), x) for x in array]
    answer = array[arr.index(min(sorted(arr)))]
    return answer