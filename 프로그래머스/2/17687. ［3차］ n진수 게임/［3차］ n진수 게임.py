def convert(value, n):
    result = ''
    
    num = ['A', 'B', 'C', 'D', 'E', 'F']
    
    if n == 10:
        return str(value)
    
    start = 17
    while value // (n ** start) == 0:
        start -= 1
    
    for i in range(start, -1, -1):
        a = value // (n ** i)
        result += str(a) if a < 10 else num[a - 10]
        value %= (n ** i)
        
    return result
                
def solution(n, t, m, p):
    answer = ''
    
    total_str = '0'
    
    i = 1
    while len(total_str) < t * m:
        total_str += convert(i, n)
        i += 1
                    
    for i in range(p - 1, p - 1 + t*m, m):
        answer += total_str[i]
        
    return answer