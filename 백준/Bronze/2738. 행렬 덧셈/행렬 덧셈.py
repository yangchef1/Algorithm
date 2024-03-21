n, m = map(int, input().split())

m1 = []
m2 = []

for i in range(n):
   m1.append(list(map(int, input().split()))) 
   
for i in range(n):
   m2.append(list(map(int, input().split())))  
   
for i in range(n):
    for j in range(m):
        print(m1[i][j] + m2[i][j], end=" ")
    print()