def solution(genres, plays):
    answer = []
    dict_cnt = {}
    dict_con = {}
    
    for idx, (ge, pl) in enumerate(zip(genres, plays)):
        if ge not in dict_cnt:
            dict_cnt[ge] = 0
        dict_cnt[ge] += pl
        
        if ge not in dict_con:
            dict_con[ge] = [(idx, pl)]
        else:
            dict_con[ge].append((idx, pl))
            
    for (k,v) in sorted(dict_cnt.items(), key=lambda x:x[1], reverse=True):
        for (idx, pl) in sorted(dict_con[k], key=lambda x:x[1], reverse=True)[:2]:
            answer.append(idx)
    
    return answer