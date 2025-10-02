def solution(files):    
    answer = []
    s_files = []
    for file in files:
        s_file = ['', '', '']
        
        i = 0
        while i < len(file):
            if file[i].isdigit():
                break
            s_file[0] += file[i]
            i += 1
        
        while i < len(file):
            if not file[i].isdigit():
                break
            s_file[1] += file[i]
            i += 1
        
        s_file[2] = file[i:]
        
        s_files.append(s_file)
        
    s_files.sort(key=lambda x : (x[0].lower(), int(x[1])))
    
    for s_file in s_files:
        answer.append(''.join(s_file))
        
    return answer