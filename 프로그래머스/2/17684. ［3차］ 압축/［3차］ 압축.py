def solution(msg):
    l = len(msg)
    answer = []
    dic = ['', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    if l == 1:
        return [dic.index(msg)]
    
    i = 0
    while i < l:
        output = 0
        
        t = 1
        for j in range(1, l):
            if i + j > l:
                t = j - 1
                break
                
            word = ''.join(msg[i:i+j])
                
            if word not in dic:
                dic.append(word)
                t = j - 1
                break
                
            output = dic.index(word)
                
        answer.append(output)
        i += t
            
    return answer