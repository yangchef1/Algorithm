def solution(numbers, target):
    answer = 0
    
    result = [[] for _ in range(len(numbers)+1)]
    result[0].append(0)
    
    for i in range(len(numbers)):
        for j in result[i]:
            result[i+1].append(j+numbers[i])
            result[i+1].append(j-numbers[i])
        
    return result[-1].count(target)