def solution(info, edges):
    answer = 0
    
    graph = {}
    for s, e in edges:
        graph[s] = graph.get(s, []) + [e]
        
    def dfs(node, sheep, wolf, can_visit):
        nonlocal answer
        
        if info[node] == 0:
            sheep += 1
        else:
            wolf += 1
        
        if answer < sheep:
            answer = sheep
            
        if sheep <= wolf:
            return
        
        nxt_node = can_visit.copy()
        nxt_node.extend(graph.get(node, []))
        if node in nxt_node:
            nxt_node.remove(node)
        
        for nxt in nxt_node:
            dfs(nxt, sheep, wolf, nxt_node)
    
    dfs(0, 0, 0, [])
    
    return answer