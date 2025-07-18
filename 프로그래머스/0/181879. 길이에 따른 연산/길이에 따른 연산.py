def fun(arr):
    res = 1
    for ele in arr:
        res *= ele
    return res
def solution(num_list):
    return sum(num_list) if len(num_list) > 10 else fun(num_list)