def g_is_safe(answer, x, y):
    return (y == 0 or [x, y, 1] in answer or [x - 1, y, 1] in answer or [x, y - 1, 0] in answer)

def b_is_safe(answer, x, y):
    return ([x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer))

def all_is_safe(answer):
    for build in answer:
        x, y, a = build
        if a == 0 and not g_is_safe(answer, x, y):
            return False
        if a == 1 and not b_is_safe(answer, x, y):
            return False
    return True

def solution(n, build_frame):
    answer = []
    
    for build in build_frame:
        x, y, a, b = build
        
        # 기둥 설치
        if b == 1 and a == 0 and g_is_safe(answer, x, y):
            answer.append([x, y, a])
        # 보 설치
        if b == 1 and a == 1 and b_is_safe(answer, x, y):
            answer.append([x, y, a])
        
        if b == 0:
            na = answer.copy()
            na.remove([x, y, a])
            if all_is_safe(na):
                answer.remove([x, y, a])            
            
    answer.sort()
    return answer