from itertools import combinations
import bisect

def solution(info, query):
    answer = []
    info_dict = {}
    
    for i in info:
        a, b, c, d, score = i.split()
        score = int(score)
        for j in range(5):
            cl = list(combinations([a, b, c, d], j))
            for cv in cl:
                ncv = info_dict.get(cv, [])
                bisect.insort(ncv, score)
                info_dict[cv] = ncv
    
    for q in query:
        a, b, c, d = q.split(' and ')
        d, score = d.split()
        score = int(score)
        
        ql = []
        for i in [a, b, c, d]:
            if i != '-':
                ql.append(i)
        ql = tuple(ql)
        
        scores = info_dict.get(ql, [])
        ls = len(scores)
        answer.append(ls - bisect.bisect_left(scores, score))
        
    return answer