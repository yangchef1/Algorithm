def solution(numbers, target):
    result = [0]
    
    for i in range(len(numbers)):
        answer = []
        for j in result:
            answer.extend([j+numbers[i], j-numbers[i]])
        result = answer.copy()
        
    return result.count(target)