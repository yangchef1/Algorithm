import heapq

def solution(n, s, a, b, fares):    
    INF = float('inf')
    dists = [[INF] * (n + 1) for _ in range(n + 1)]
    
    for i in range(n + 1):
        dists[i][i] = 0
        
    for fare in fares:
        c, d, fee = fare
        dists[c][d] = fee
        dists[d][c] = fee
    
    for k in range(n + 1):
        for i in range(n + 1):
            for j in range(n + 1):
                if dists[i][j] > dists[i][k] + dists[k][j]:
                    dists[i][j] = dists[i][k] + dists[k][j]
    
    answer = min(dists[s][a] + dists[s][b], dists[s][a] + dists[a][b], dists[s][b] + dists[b][a])
    for i in range(n + 1):
        v = dists[s][i] + dists[i][a] + dists[i][b]
        if v < answer:
            answer = v
    
    
    return answer