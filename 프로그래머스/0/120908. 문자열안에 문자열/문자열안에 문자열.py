def solution(str1, str2):
    cnt = 0
    answer = 2
    for i in range(len(str1) - len(str2) + 1):
        if str1[i] == str2[0]:
            cnt = 0
            for j in range(len(str2)):
                if str1[i+j] == str2[j]:
                    cnt += 1
                else:
                    break
            if cnt == len(str2):
                answer = 1
    return answer