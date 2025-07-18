def solution(clothes):
    hash_map = {}
    for _, categ in clothes:
        if categ not in hash_map:
            hash_map[categ] = 0
        hash_map[categ] += 1
    
    answer = 1
    for i in hash_map.values():
        answer *= (i + 1)
    
    return answer - 1