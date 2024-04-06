odd = []
for i in range(7):
    a = int(input())
    if a % 2 == 1:
        odd.append(a)

if odd: 
    print(sum(odd))
    print(min(odd))
else:
    print(-1)