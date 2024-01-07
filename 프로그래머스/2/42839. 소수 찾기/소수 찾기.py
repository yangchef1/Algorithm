from itertools import permutations

def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
        
def solution(numbers):
    answer = []
    
    for i in range(1, len(numbers) + 1):
        for permutation in permutations(numbers, i):
            number = int("".join(map(str, permutation)))
            if is_prime(number) and (number not in answer):
                answer.append(number)
    return len(answer)