import sys

n = int(input())

company = set()

for _ in range(n):
    name, io = sys.stdin.readline().split()
    
    if io == 'enter':
        company.add(name)
    else:
        company.remove(name) 

print('\n'.join(sorted(company, reverse=True)))