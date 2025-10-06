def is_ok(string):
    stack = []
    
    for s in string:
        if stack and stack[-1] == '(' and s == ')':
            stack.pop()
        else:
            stack.append(s)
            
    return len(stack) == 0

def split_uv(p):
    if p == '':
        return p
    
    u, v = '', ''
    r_cnt, l_cnt = 0, 0
    for i in range(len(p)):
        if r_cnt != 0 and r_cnt == l_cnt:
            v = p[i:]
            break
        
        s = p[i]
        if s == '(':
            r_cnt += 1
        if s == ')':
            l_cnt += 1
        
        u += s
    
    result = split_uv(v)
    
    if is_ok(u):
        return u + result
        
    base_str = '(' + result + ')'
    
    return base_str + ''.join(map(lambda x: '(' if x == ')' else ')', u[1:-1]))

def solution(p):
    if is_ok(p):
        return p

    return split_uv(p)