a = list(input())
b = list(input())
a_cnt = 0
b_cnt = len(b)

for i in a:
    if i not in b:
        a_cnt += 1
    else:
        b.remove(i)
        b_cnt -= 1

print(a_cnt + b_cnt)