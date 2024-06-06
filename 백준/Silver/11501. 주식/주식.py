t = int(input())

for _ in range(t):
    d = int(input())
    price = list(map(int, input().split()))
    stock, cnt = 0, 0
    max_val = max(price)
    result = 0
    
    for i in range(d):        
        if price[i] != max_val:
            stock += price[i]
            cnt += 1
        elif price[i - 1] != price[i]:
            result += ((price[i] * cnt) - stock)
            stock, cnt = 0, 0
            max_val = max(price[i + 1:] + [-1])
                        
    print(result)