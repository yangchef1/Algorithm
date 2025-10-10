def solution(board, skill):
    m, n = len(board), len(board[0])
    answer = 0
    
    change = [[0 for _ in range(n)] for _ in range(m)]
    
    for type, a, b, c, d, degree in skill:
        degree *= 1 if type == 2 else -1
        change[a][b] += degree
        if d + 1 < n:
            change[a][d + 1] -= degree
        if c + 1 < m:
            change[c + 1][b] -= degree
        if d + 1 < n and c + 1 < m:
            change[c + 1][d + 1] += degree
    
    for i in range(m):
        for j in range(1, n):
            change[i][j] += change[i][j  - 1]
            
    for i in range(1, m):
        for j in range(n):
            change[i][j] += change[i - 1][j]
    
    for i in range(m):
        for j in range(n):
            board[i][j] += change[i][j]
            if board[i][j] > 0:
                answer += 1
    
    return answer