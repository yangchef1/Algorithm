from collections import deque

def bfs(visited, dis, start, dest):
    need_visited = deque([start])
    dis[start] = 0
    visited[start] = True
    
    while need_visited:
        node = need_visited.popleft()
        
        temp = [node * 2, node - 1, node + 1]
        
        for i in temp:
            if i <= 100000 and i >= 0 and not visited[i]:
                visited[i] = True
                need_visited.append(i)
                
                if i == node * 2:
                    dis[i] = min(dis[i], dis[node])
                else:
                    dis[i] = min(dis[i], dis[node] + 1)

s, d = map(int, input().split())
visited = [False] * 100001
dis = [float('inf')] * 100001

bfs(visited, dis, s, d)

print(dis[d])