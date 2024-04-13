t = int(input())
result = []

for i in range(t):
    a, b = map(int, input().split())
    k = ((a%10)**(b%4 + 4))%10
    result.append(k if k != 0 else 10)

print("\n".join(map(str, result)))