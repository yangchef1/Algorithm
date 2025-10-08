import math

def convert_k(n, k):
    result = ''
    
    while n > 0:
        result = result + str(n % k)
        n = n // k
        
    return result[::-1]

def is_prime(n):  
    n = int(n)
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    
    k_num = convert_k(n, k)
    nums = k_num.split('0')
    
    for num in nums:
        if num.isdigit() and int(num) > 1 and is_prime(num):
            answer += 1
    
    return answer