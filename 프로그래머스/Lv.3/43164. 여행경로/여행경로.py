def dfs(graph):
    need_visited = ["ICN"]
    result = []
    
    while need_visited:
        node = need_visited[-1]
        
        if node not in graph or len(graph[node]) == 0:
            result.append(need_visited.pop())
        else:
            need_visited.append(graph[node].pop())
        
    return result[::-1]

def solution(tickets):
    graph = {}
    
    for ticket in tickets:
        if ticket[0] not in graph:
            graph[ticket[0]] = [ticket[1]]
        else:
            graph[ticket[0]].append(ticket[1])
    
    for ticket in graph.values():
        ticket.sort(reverse=True)
    
    return dfs(graph)