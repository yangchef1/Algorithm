N, B = input().split()
N = list(map(lambda x : ord(x) - 55 if x.isalpha() else int(x), N)) 
N.reverse()
B = int(B)
result = 0

for i in range(len(N)):
    result += N[i] * (B**i)
    
print(result)