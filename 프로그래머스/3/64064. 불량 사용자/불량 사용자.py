from itertools import product

def compare(b_id, u_id):
    if len(b_id) != len(u_id):
        return False
    
    for a, b in zip(b_id, u_id):
        if a != '*' and a != b:
            return False
    return True
    
def solution(user_id, banned_id):   
    answer = 0
    result = []
    cnt = []
    
    for b_id in banned_id:
        matched = []
        for u_id in user_id:
            if compare(b_id, u_id):
                matched.append(u_id)
        cnt.append(matched)
    
    need_visited = [[[cnt[0][i]], 0] for i in range(len(cnt[0]))]
    
    while need_visited:
        path, d = need_visited.pop()
        
        if d >= len(cnt) - 1:
            sn = set(path)
            if len(path) == len(banned_id) and sn not in result:
                answer += 1
                result.append(sn)
            continue
        
        for i in cnt[d + 1]:
            if i not in path:
                need_visited.append([path + [i], d + 1])
                
    return answer