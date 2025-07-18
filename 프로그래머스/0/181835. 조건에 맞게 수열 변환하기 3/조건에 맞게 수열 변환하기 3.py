def solution(arr, k):
    answer = []
    for ele in arr:
        if k % 2 == 0:
            answer.append(ele+k)
        else:
            answer.append(ele*k)
    return answer