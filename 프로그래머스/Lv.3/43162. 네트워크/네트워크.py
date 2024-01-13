def dfs (graph, start, visited):
    need_visited = [start]

    while need_visited:
        node = need_visited.pop()
        if not visited[node]:
            visited[node] = True
            for i in range(len(graph[node])):
                if graph[node][i] == 1 and not visited[i]:
                    need_visited.append(i)
            
def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    for i in range(n):
        if not visited[i]:
            dfs(computers, i, visited)
            answer += 1
            
    return answer