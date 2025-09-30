def solution(friends, gifts):
    answer = 0
    table = {}
    score = {}
    result = {}
    
    for i in friends:
        temp = {}
        for j in friends:
            temp[j] = 0
        table[i], score[i], result[i] = temp, 0, 0
    
    for g in gifts:
        a, b = g.split()
        table[a][b] += 1
        score[a] += 1
        score[b] -= 1
    
    for i in friends:
        for j in friends:
            if i == j:
                continue
                
            if table[i][j] > table[j][i] or (table[i][j] == table[j][i] and score[i] > score[j]):
                result[i] += 1
                    
    return max(result.values())