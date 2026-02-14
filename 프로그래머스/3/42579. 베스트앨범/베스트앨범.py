"""
[문제]
장르와 조회수가 주어졌을 때, 장르별 최대 2개의 곡을 반환
장르 전체 조회수가 높은 순으로 정렬 후 해당 장르 내에서 조회수 순으로 선정
결과는 선정된 곡의 ID를 반환(ID: 곡의 입력 순서)

[해석]
ID가 없기 때문에 zip()과 enumerate()를 활용하여 ID 생성
장르에 대한 정렬과 조회수에 대한 정렬을 수행해야 함

[풀이]
장르 계산과 아이디 복원용 딕셔너리 생성 후 값 저장
sorted 정렬 및 lamdba를 활용한 조건부 정렬 수행
슬라이싱을 이용해 각 장르별 곡을 선정 후 반환
"""
def solution(genres, plays):
    answer = []
    dict_genre = {} # {장르: 조회수 합}
    dict_idx = {} # {장르: (아이디, 조회수)}
    
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        # Solving 1: 장르별 조회수 병합
        if genre not in dict_genre:
            dict_genre[genre] = 0
        dict_genre[genre] += play
        
        # Solving 2: 아이디와 조회수 매핑 후 저장
        if genre not in dict_idx:
            dict_idx[genre] = [(idx, play)]
        else:
            dict_idx[genre].append((idx, play))
    
    # Solving 3: 장르별 조회수 순으로 정렬
    for k, _ in sorted(dict_genre.items(), key=lambda x: -x[1]):
        # Solving 4: 장르 내 조회수 순으로 정렬, 같으면 idx 작은 순으로 정렬
        for idx, _ in sorted(dict_idx[k], key=lambda x: (-x[1], x[0]))[:2]:
            answer.append(idx)
    
    return answer