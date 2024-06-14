n = int(input())
l = len(str(n))
result = 0

for i in range(1, l):
    result += 9 * i * (10 ** (i - 1))
    
result += l * (n - int("9" * (l - 1) if l > 1 else 0))

print(result)