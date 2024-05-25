t = int(input())
for _ in range(t):
    n = int(input())
    univ = {}
    for _ in range(n):
        name, drink = input().split()
        univ[int(drink)] = name
    print(univ[max(univ.keys())])