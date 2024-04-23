string = input()
alph = {}

for i in string:
    a = alph.get(i, None)
    if a == None:
        alph[i] = 1  
    else:
        alph[i] += 1

even_num, odd_num, odd_cnt = "", "", 0

alph = sorted(alph.items(), key=lambda x : x[0])

for apb, cnt in alph:
    if cnt % 2 == 1:
        odd_cnt += 1
        odd_num += apb
        even_num += (apb * (cnt // 2))
        if odd_cnt >= 2:
            print("I'm Sorry Hansoo")
            exit(0)
    else:
        even_num += (apb * (cnt // 2))
        
print(even_num + odd_num +even_num[::-1])