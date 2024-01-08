from itertools import product

def solution(word):
    answer = 0
    alpha = "AEIOU"
    words = []
    for i in range(1, 6):
        for w in product(alpha, repeat=i):
            words.append("".join(map(str, w)))
                
    words.sort()
    for i in range(len(words)):
        if words[i] == word:
            answer = i + 1
    
    return answer