from itertools import product

def compare(b_id, u_id):
    if len(b_id) != len(u_id):
        return False
    
    for a, b in zip(b_id, u_id):
        if a != '*' and a != b:
            return False
    return True
        
def solution(user_id, banned_id):    
    cnt = []
    
    for b_id in banned_id:
        matched = []
        for u_id in user_id:
            if compare(b_id, u_id):
                matched.append(u_id)
        cnt.append(matched)
    
    cases = product(*cnt)
    result = set()
    
    for case in cases:
        if len(set(case)) == len(banned_id):
            result.add(frozenset(case))
        
    return len(result)