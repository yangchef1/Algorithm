def solution(board):
    answer = 0
    n = len(board)
    
    shapes = [
        ([(0, 0), (0, 1), (1, 1), (2, 1)], [(1, 0), (2, 0)]),
        ([(0, 2), (1, 0), (1, 1), (1, 2)], [(0, 0), (0, 1)]),
        ([(2, 0), (2, 1), (1, 1), (0, 1)], [(0, 0), (1, 0)]),
        ([(0, 0), (0, 1), (0, 2), (1, 2)], [(1, 0), (1, 1)]),
        ([(1, 0), (0, 1), (1, 1), (2, 1)], [(0, 0), (2, 0)])
    ]
    
    prev_break = -1
    while prev_break < answer:
        prev_break = answer
        for y in range(n):
            for x in range(n):
                b = board[y][x]
                for shape in shapes:
                    can_break = True
                    prev_value = []
                    for fill in shape[0]:
                        nx, ny = x + fill[0], y + fill[1]
                        if nx < 0 or ny < 0 or nx >= n or ny >= n:
                            can_break = False
                            break
                        if board[ny][nx] == 0 or (prev_value and board[ny][nx] not in prev_value):
                            can_break = False
                            break
                        prev_value.append(board[ny][nx])
                    for blank in shape[1]:
                        nx, ny = x + blank[0], y + blank[1]
                        if nx < 0 or ny < 0 or nx >= n or ny >= n:
                            can_break = False
                            break
                        if board[ny][nx] != 0:
                            can_break = False
                            break
                    for blank in shape[1]:
                        for i in range(y - 1, -1, -1):
                            nx = x + blank[0]
                            if nx < 0 or nx >= n:
                                can_break = False
                                break
                            if board[i][nx] != 0:
                                can_break = False
                                break
                    if can_break:
                        for fill in shape[0]:
                            nx, ny = x + fill[0], y + fill[1]
                            board[ny][nx] = 0
                        answer += 1
                        break

    return answer