def solution(num_list):
    even = [num for num in num_list if num % 2 == 0]
    odd = [num for num in num_list if num % 2 != 0]
    answer = [len(even), len(odd)]
    return answer