def contain(main, sub):
    lm, ls = len(main), len(sub)
    for i in range(lm - ls + 1):
        if main[i:i + ls] == sub:
            return True
    return False

def solution(m, musicinfos):
    result = []
    
    for musicinfo in musicinfos:
        start, end, name, melody = musicinfo.split(',')
        
        sh, sm = start.split(':')
        eh, em = end.split(':')
        
        time = (int(eh) - int(sh)) * 60 + (int(em) - int(sm))
        
        music_len = 0
        melody_list = []
        
        for i in melody:
            if i.isalpha():
                music_len += 1
                melody_list.append(i)
            else:
                melody_list[-1] += i
        
        total_list = melody_list * (time // music_len) + melody_list[:time % music_len]

        m_list = []
        for i in m:
            if i.isalpha():
                m_list.append(i)
            else:
                m_list[-1] += i
        
        if contain(total_list, m_list):
            result.append([time, name])
            
    if not result:
        return "(None)"
    
    result.sort(key=lambda x: x[0], reverse=True)
    
    return result[0][1]