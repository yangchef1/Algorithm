def solution(brown, yellow):
    answer = []
    total = brown+yellow
    
    for i in range(1, total // 2 + 1):
        if (i + (total / i)) * 2 - 4 == brown and (i not in answer):
            answer.append(i)
            answer.append(int(total/i))
            
    answer.sort(reverse=True)       
    return answer