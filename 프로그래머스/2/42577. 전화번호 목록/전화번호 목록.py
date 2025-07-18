def solution(phone_book):
    cnt = 0
    dic = dict()
    for i in range(len(phone_book)):
        dic[phone_book[i]] = i
    for i in range(len(phone_book)):
        for j in range(len(phone_book[i])):
            cnt += 1
            if phone_book[i][0:j] in dic:
                print(cnt)
                return False
    return True