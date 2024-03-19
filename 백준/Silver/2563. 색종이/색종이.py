n = int(input())
papers = []

for i in range(n):
    papers.append(list(map(int, input().split())))
    
graph = [[0] * 100 for _ in range(100)]

for paper in papers:
    for i in range(10):
        for j in range(10):
            graph[paper[0] + i][paper[1] + j] = 1
            
result = 0

for i in graph:
    result += i.count(1)
    
print(result)