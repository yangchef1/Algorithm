n = int(input())
rope = []
max_value = 0

for _ in range(n):
    rope.append(int(input()))
    
rope.sort()

for i in range(n):
    max_value = max(max_value, rope[i] * (n - i))
    
print(max_value)        