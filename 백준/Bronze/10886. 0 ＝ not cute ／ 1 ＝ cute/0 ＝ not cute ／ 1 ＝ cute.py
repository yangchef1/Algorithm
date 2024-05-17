n = int(input())
op = []

for _ in range(n):
    op.append(int(input()))
    
print( "Junhee is not cute!" if op.count(0) > op.count(1) else  "Junhee is cute!")