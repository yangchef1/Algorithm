from itertools import combinations

def solution(relation):
    l = len(relation)
    answer = 0
    
    result = []
    cl = len(relation[0])
    
    ci = list(range(1, cl + 1))
    for i in range(1, cl + 1):
        comb = combinations(ci, i)
        for c in comb:
            print(len(set(map(lambda x : tuple(x[i - 1] for i in c), relation))))
            if len(set(map(lambda x : tuple(x[i - 1] for i in c), relation))) == l:
                is_exist = False
                cs = set(c)
                for r in result:
                    if r.issubset(cs):
                        is_exist = True
                        break
                if not is_exist:
                    result.append(cs)
                    answer += 1
                print(result)
    
    return answer