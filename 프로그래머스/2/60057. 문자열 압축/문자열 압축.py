def solution(s):
    l = len(s)
    min = l
    
    for window in range(1, l + 1):
        ls = []
        for i in range(0, l, window):
            ls.append(s[i:i + window] if i + window <= l else s[i:])
            
        result = ''
        i= 0
        while i < len(ls):
            for j in range(1, len(ls) - i + 1):
                if i + j >= len(ls):
                    result += (str(j) + ls[i]) if j > 1 else ls[i]
                    i += j
                    break
                    
                if ls[i] != ls[i + j]:
                    result += (str(j) + ls[i]) if j > 1 else ls[i]
                    i += j
                    break
            
        if result and min > len(result):
            min = len(result)
            
    return min