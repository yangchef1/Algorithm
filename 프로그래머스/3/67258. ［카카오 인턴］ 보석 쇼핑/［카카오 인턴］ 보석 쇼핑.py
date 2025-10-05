from collections import deque

def solution(gems):
    l = len(gems)
    answer = [1, l]
    count = len(set(gems))
    
    type = deque()
    
    left = 0
    for right in range(l):
        type.append(gems[right])
        while len(set(type)) == count:
            left += 1
            type.popleft()
            if answer[1] - answer[0] > right - left:
                answer = [left + 1, right + 1]
                break
        
    return answer