from collections import deque

def bfs(place, start):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    need_visited = deque([start])
    dis = [[-1 for _ in range(5)] for _ in range(5)]
    dis[start[0]][start[1]] = 0
    
    while need_visited:
        x, y = need_visited.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if nx >= 0 and ny >= 0 and nx < 5 and ny < 5 and dis[nx][ny] == -1 and place[nx][ny] != "X":
                dis[nx][ny] = dis[x][y] + 1
                
                if 1 <= dis[nx][ny] <= 2 and place[nx][ny] == "P":              
                    return False
                need_visited.append([nx, ny])
    return True

def solution(places):
    answer = [1, 1, 1, 1, 1]
    
    for i in range(5):
        for x in range(5):
            for y in range(5):
                if places[i][x][y] == "P" and not bfs(places[i], [x, y]):
                    answer[i] = 0
                    break
                
    return answer