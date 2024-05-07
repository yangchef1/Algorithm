a = sorted(list(map(int, input().split()))) 
print(a[0] + a[1] + (a[0] + a[1] - 1 if a[2] >= a[0] + a[1] else a[2]))