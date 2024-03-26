from decimal import getcontext, ROUND_HALF_UP, Decimal

context = getcontext()
context.rounding = ROUND_HALF_UP

n = int(input())
coordinates = []
result = 0

for _ in range(n):
    coordinates.append(list(map(int, input().split())))

for i in range(-1, len(coordinates) - 1):
    result += coordinates[i][0] * coordinates[i+1][1]
    result -= coordinates[i][1] * coordinates[i+1][0]
    
print(round(Decimal(str(abs(result/2))), 1))