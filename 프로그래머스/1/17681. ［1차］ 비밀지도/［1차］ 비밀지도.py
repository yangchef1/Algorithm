def d_to_b(d, n):
    result = []
    
    for i in range(n - 1, -1, -1):
        result.append(d // (2**i))
        d %= (2**i)
        
    return result

def solution(n, arr1, arr2):
    answer = []
    map1 = []
    map2 = []
    
    for i, j in zip(arr1, arr2):
        map1.append(d_to_b(i, n))
        map2.append(d_to_b(j, n))
    
    for i in range(n):
        row = ""
        for j in range(n):
            row += "#" if map1[i][j] == 1 or map2[i][j] == 1 else " "
        answer.append(row)
    
    return answer