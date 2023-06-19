sum1 = 0
sum2 = 0

for i in range(20):
    flag = 0
    a, b, c = input().split()
    
    if c == "P":
        flag = 1
    
    score = 0
    
    if c == "A+":
        score = 4.5
    elif c == "A0":
        score = 4.0
    elif c == "B+":
        score = 3.5
    elif c == "B0":
        score = 3.0
    elif c == "C+":
        score = 2.5
    elif c == "C0":
        score = 2.0
    elif c == "D+":
        score = 1.5
    elif c == "D0":
        score = 1.0
    elif c == "F":
        score = 0.0
    
    if flag == 0:
        sum1 += float(b)*score
        sum2 += float(b)
    
print(sum1/sum2)
    
