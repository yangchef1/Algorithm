x, y = [0] * 3, [0] * 3
for i in range(3):
    x[i], y[i] = map(int, input().split())
    
print(x[0] ^ x[1] ^ x[2], y[0] ^ y[1] ^ y[2]) 