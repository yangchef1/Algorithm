n = int(input())
Y, M = 0, 0

time = list(map(int, input().split()))

for i in time:
    Y += (i // 30 + 1) * 10
    M += (i // 60 + 1) * 15
    
if Y > M:
    print("M", M)
elif M > Y:
    print("Y", Y)
else:
    print("Y", "M", Y)