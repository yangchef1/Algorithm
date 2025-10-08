def convert_int(time):
    h, m, s = map(int, time.split(':'))
    return h * 3600 + m * 60 + s
    
def solution(play_time, adv_time, logs):
    answer = 0
    
    pt = convert_int(play_time)
    at = convert_int(adv_time)
    
    if pt == at:
        return '00:00:00'
    
    dv = [0] * (pt + 1)
    
    for log in logs:
        s, e = map(convert_int, log.split('-'))
        dv[s] += 1
        dv[e] -= 1
    
    video = [0] * (pt + 1)
    video[0] = dv[0]
    for i in range(1, pt + 1):
        video[i] = video[i - 1] + dv[i]
    
    sv = [0] * (pt + 1)
    sv[0] = video[0]
    for i in range(1, pt + 1):
        sv[i] = sv[i - 1] + video[i - 1]
    
    m = 0
    for i in range(pt - at + 1):
        total = sv[i + at] - sv[i]

        if total > m:
            m = total
            answer = i
            
    return f'{answer // 3600:02}:{(answer % 3600) // 60:02}:{(answer % 3600) % 60:02}'