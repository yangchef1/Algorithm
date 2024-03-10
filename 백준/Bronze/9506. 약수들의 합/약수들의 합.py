while True:
    n = int(input())
    
    if n == -1:
        break
    
    divisor = []
    
    for i in range(1, n):
        if n % i == 0:
            divisor.append(i)

    if n == sum(divisor):
        print(n, "= ", end="")
        print(" + ".join(map(str, divisor)))
    else:
        print(n, "is NOT perfect.")