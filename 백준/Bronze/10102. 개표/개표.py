n = int(input())
s = input()
a, b = s.count('A'), s.count('B')

if a == b:
    print('Tie')
else:
    print('A' if a > b else 'B')