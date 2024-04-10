n, k = map(int, input().split())

room = [[0] * 2 for _ in range(7)]

for i in range(n):
    s, y = map(int, input().split())   
    room[y][s] += 1

result = 0

for i in range(1, 7):
    for j in range(2):
        if room[i][j] != 0:
            result += ((room[i][j] - 1) // k) + 1
    
print(result)