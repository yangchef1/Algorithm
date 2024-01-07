import math

def solution(brown, yellow):
    answer = []
    sum = brown//2 + 2
    product = brown + yellow
    
    answer.append(int(sum/2 + math.sqrt(((sum/2)**2) - product)))
    answer.append(int(sum/2 - math.sqrt(((sum/2)**2) - product)))
    return answer