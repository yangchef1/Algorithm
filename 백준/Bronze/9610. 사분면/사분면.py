n = int(input())
result = []

for i in range(n):
    a, b = map(int, input().split())
    
    if a > 0 and b > 0:
        result.append(1)
    elif a < 0 and b > 0:
        result.append(2)
    elif a < 0 and b < 0:
        result.append(3)
    elif a > 0 and b < 0:
        result.append(4)
    else:
        result.append(5)
        
for i in range(1, 5):
    print("Q{0}: {1}".format(i, result.count(i)))
print("AXIS:", result.count(5))