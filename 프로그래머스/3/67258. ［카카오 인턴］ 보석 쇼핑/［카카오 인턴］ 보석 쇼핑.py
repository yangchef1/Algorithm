def solution(gems):
    l = len(gems)
    answer = [1, l]
    count = len(set(gems))
    
    g_count = {}
        
    left = 0
    for right in range(l):
        g_count[gems[right]] = g_count.get(gems[right], 0) + 1
        while len(g_count) == count:
            if answer[1] - answer[0] > right - left:
                answer = [left + 1, right + 1]
            g_count[gems[left]] -= 1
            if g_count.get(gems[left], 0) == 0:
                del g_count[gems[left]]
            left += 1
        
    return answer