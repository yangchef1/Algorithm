N, B = map(int, input().split())
result = ""
k = 0
while B ** k <= N:
    k += 1    

for i in range(k-1, -1, -1):
    result += str(N//(B ** i)) if N//(B**i) < 10 else chr(N// (B ** i) + 55) 
    N %= B ** i
    
print(result)