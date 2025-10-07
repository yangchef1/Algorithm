"""

"""
from itertools import combinations

def solution(orders, course):
    answer = []
    
    combs = {}
    for c in course:
        combs[c] = {}
    
    
    for order in orders:
        ol = list(order)
        for cnt in course:
            for comb in list(combinations(ol, cnt)):
                cs = frozenset(comb)
                combs[cnt][cs] = combs[cnt].get(cs, 0) + 1

    for comb in combs.values():
        cv = comb.values()
        if len(cv) == 0:
            continue
        m = max(cv)
        for cs, cnt in comb.items():
            if cnt == m and cnt >= 2:
                cl = list(cs)
                cl.sort()
                c = ''.join(cl)
                answer.append(c)
                
    answer.sort()
    return answer