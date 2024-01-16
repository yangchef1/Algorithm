from collections import deque

def strcmp(first, second):
    unmatch = 0
    
    for f, s in zip(first, second):
        if f != s:
            unmatch += 1
            
    return unmatch

def bfs(start, end, graph):
    need_visited = deque()
    need_visited.append((start, 0))
    visited = set()
    
    while need_visited:
        node, dis = need_visited.popleft()
        
        if node == end:
            return dis
        
        if node not in visited:
            visited.add(node)
            neighbors = graph.get(node, [])
            need_visited.extend([(word, dis + 1) for word in neighbors])
         
    return 0

def solution(begin, target, words):
    answer = 0
    graph = {}
    
    visited = {word : False for word in words}
    visited[begin] = False
    need_visited = [begin]
    
    while need_visited:
        current_word = need_visited.pop()
    
        for word in words:
            if strcmp(current_word, word) == 1:
                if current_word in graph and word not in graph[current_word]:
                    graph[current_word].append(word)
                else:
                    graph[current_word] = [word]
        
                if not visited[word]:
                    visited[word] = True
                    need_visited.append(word)
    
    return bfs(begin, target, graph)
