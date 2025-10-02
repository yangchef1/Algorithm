def solution(dartResult):
    l = len(dartResult)
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    s = {"S" : 1, "D" : 2, "T" : 3}
    
    dart = []
    i = 0
    while i < l:
        d = dartResult[i]
        if d == "1" and dartResult[i + 1] == "0":
            score = dartResult[i:i+3]
            dart.append(int(score[:-1])**s[score[-1]])
            i += 3
        elif d in num:
            score = dartResult[i:i+2]
            dart.append(int(score[:-1])**s[score[-1]])
            i += 2
        elif d == "*" or d == "#":
            dart.append(dartResult[i])
            i += 1

    i = 0
    while i < len(dart):
        if dart[i] == "*":
            if i > 1:
                dart[i - 2] *= 2
            dart[i - 1] *= 2
            del dart[i]
        elif dart[i] == "#":
            dart[i - 1] *= -1
            del dart[i]
        else:
            i += 1
    
    return sum(dart)