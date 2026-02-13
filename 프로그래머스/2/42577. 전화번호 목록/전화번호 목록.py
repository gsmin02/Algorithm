"""
[문제]
입력된 번호가 다른 번호의 접두어인 경우 false 아니면 true를 반환

[해석]
전화번호를 가져와 해당 번호로 시작하는 다른 번호가 있는지 확인

[풀이]
전화번호 추출 후 문자열을 더해서 원본과 비교
> 본인과 같은 경우는 제외
"""
def solution(phone_book):
    hash_phone = {}
    for phone_number in phone_book:
        hash_phone[phone_number] = True
    for phone_number in phone_book:
        diff = ""
        for number in phone_number:
            diff += number
            if diff in hash_phone and diff != phone_number:
                return False
    return True