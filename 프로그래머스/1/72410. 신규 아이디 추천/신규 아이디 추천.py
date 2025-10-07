def solution(new_id):
    answer = ''
    for w in new_id.lower():
        if not w.isalpha() and not w.isdigit() and w not in ['-', '_', '.']:
            continue
        
        if w == '.' and answer and answer[-1] == '.':
            continue 
        
        answer += w
    
    if answer and answer[0] == '.':
        answer = answer[1:]
    if answer and answer[-1] == '.':
        answer = answer[:-1]
        
    if not answer:
        answer += 'a'
        
    if len(answer) >= 16:
        answer = answer[:15]
        
    if answer and answer[-1] == '.':
        answer = answer[:-1]
    
    last = answer[-1]
    while len(answer) <= 2:
        answer += last
        
    return answer