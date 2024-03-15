from itertools import combinations

def strcmp(s1, s2):
    cnt = 4
    for i in range(4):
        if s1[i] == s2[i]:
            cnt -= 1
            
    return cnt

t = int(input())
result = []

for _ in range(t):
    n = int(input())
    mbti = list(input().split())
    
    if n >= 48:
        result.append(0)
        continue
    
    sum = 100

    for comb in combinations(mbti, 3):
        sum = min(sum, strcmp(comb[0], comb[1]) + strcmp(comb[0], comb[2]) + strcmp(comb[1], comb[2]))
    
    result.append(sum)

print("\n".join(map(str, result))) 
    