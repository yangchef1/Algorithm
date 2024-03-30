a, b = map(int,input().split())
g = a*b
while b > 0:
    a, b = b, a%b
print(int(g / a))