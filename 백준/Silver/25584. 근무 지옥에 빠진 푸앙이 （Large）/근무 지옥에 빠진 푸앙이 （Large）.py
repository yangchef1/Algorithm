n = int(input())

dic = {}

for _ in range(n):
    day1 = input().split()
    day2 = input().split()
    day3 = input().split()
    day4 = input().split()
    
    for a, b, c, d in zip(day1, day2, day3, day4):
        if a == "-" or b == "-" or c == "-" or d == "-":
            continue
        dic[a] = dic.setdefault(a, 0) + 4
        dic[b] = dic.setdefault(b, 0) + 6
        dic[c] = dic.setdefault(c, 0) + 4
        dic[d] = dic.setdefault(d, 0) + 10  
        
times = dic.values()
if len(times) == 0 or max(times) - min(times) <= 12:
    print("Yes")
else:
    print("No")
    
    