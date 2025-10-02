def solution(str1, str2):
    answer = 0
    str1, str2 = str1.lower(), str2.lower()
    
    list1 = []
    for i in range(len(str1)):
        word = str1[i:i + 2]
        if word.isalpha() and len(word) == 2:
            list1.append(word)
            
    list2 = []
    for i in range(len(str2)):
        word = str2[i:i + 2]
        if word.isalpha() and len(word) == 2:
            list2.append(word)
            
    if not list1 and not list2:
        return 65536 
            
    total = list1 + list2
    inter = []
    
    for e in total:
        if e in list1 and e in list2:
            inter.append(e)
            list1.remove(e)
            list2.remove(e)
    
    answer = len(inter) / (len(total) - len(inter))
    
    return int(answer * 65536)