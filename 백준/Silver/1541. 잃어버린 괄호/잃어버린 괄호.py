import sys

li = list(sys.stdin.readline().rstrip().split('-'))

for i in range(len(li)):
    li[i] = list(li[i].split('+'))


for i in range(len(li)):
    sum = 0
    for j in li[i]:
        sum += int(j)
    li[i] = sum

result = li[0]
for i in range(1,len(li)):
    result -= li[i]

print(result)