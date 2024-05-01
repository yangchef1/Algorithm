s = int(input())
sum, cnt = 0, 1

while True:
    if sum > s - cnt:
        break
    sum += cnt
    cnt += 1
       
print(cnt - 1)