arr = []

while True:
    try:
        arr.append(input())
    except:
        break

for i in arr:
    print(i)