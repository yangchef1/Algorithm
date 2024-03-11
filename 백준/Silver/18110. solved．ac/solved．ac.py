import sys

def round_half_up(number, decimals=0):
    multiplier = 10 ** decimals
    return int(int(number * multiplier + 0.5) / multiplier)

n = int(input())
score = []

for i in range(n):
    score.append(int(sys.stdin.readline().rstrip()))
    
score.sort()
    
score = score[round_half_up(n * 3 / 20) : n - round_half_up(n * 3 / 20)]
    
if n == 0:
    print(0) 
else:
    print(round_half_up(sum(score)/len(score)))