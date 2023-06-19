arr = []
sum = 0

for i in range(5):
    a = int(input())
    arr.append(a)
    sum += a
    
arr.sort()

print(sum//5)
print(arr[2])