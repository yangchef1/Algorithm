words = [[""]*15 for _ in range(5)]

for i in range(5):
    w = list(input())
    for j in range(len(w)):
        words[i][j] = w[j]
        
result = ""

for i in range(15):
    for j in range(5):
        result += words[j][i]
        
print(result)