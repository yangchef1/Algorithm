from itertools import combinations

dwarf = []

for _ in range(9):
    dwarf.append(int(input()))
    
for comb in combinations(dwarf, 7):
    if sum(comb) == 100:
        print("\n".join(map(str, sorted(comb))))
        break