import math

def convert_time(time):
    h, m = map(int, time.split(':'))
    
    return h * 60 + m

def solution(fees, records):
    END = 60 * 24 - 1
    bt, bf, ut, uf = map(int, fees)
    
    answer = []
    
    inout = {}
    for record in records:
        time, num, io = record.split()
        time, num = convert_time(time), int(num)
        if io == 'IN':
            inout[num] = inout.get(num, []) + [[time, END]]
        else:
            inout[num][-1][1] = time
    
    times = {}
    for n, log in inout.items():
        for io in log:
            s, e = io
            times[n] = times.get(n, 0) + (e - s)
        
    fares = {}
    for n, t in times.items():
        f = bf if t <= bt else math.ceil((t - bt) / ut) * uf + bf
        fares[n] = fares.get(n, 0) + f

    a = list(fares.items())
    a.sort(key=lambda x : x[0])
    
    return list(map(lambda x: x[1], a))