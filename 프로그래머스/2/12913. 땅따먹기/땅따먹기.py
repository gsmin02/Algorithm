def solution(land):
    for i in range(1, len(land)):
        for j in range(4):
            num = 0
            for k in range(4):
                if k != j:
                    num = max(num, land[i-1][k])
            land[i][j] += num
    return max(land[len(land)-1])