def solution(m, n, board):
    answer = 0
    
    board = list(map(list, board))
    
    c = -1
    while c != 0:
        deletes = []
    
        for i in range(m - 1):
            for j in range(n - 1):
                b = board[i][j]
                if  b != '0' and b == board[i + 1][j] and b == board[i][j + 1] and b == board[i + 1][j + 1]:
                    for k in [(i, j), (i + 1, j), (i, j + 1), (i + 1, j + 1)]:
                        if k not in deletes:
                            deletes.append(k)

        for d in deletes:
            x, y = d
            for i in range(x, 0, -1):
                board[i][y] = board[i - 1][y]
            board[0][y] = '0'
            
        answer += len(deletes)
        c = len(deletes)
    
    return answer