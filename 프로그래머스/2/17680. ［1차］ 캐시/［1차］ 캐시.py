from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque()
    cities = map(lambda x:x.lower(), cities)
    
    for city in cities:
        if city not in cache:
            answer += 5
            cache.append(city)
            if len(cache) > cacheSize:
                cache.popleft()
        else:
            answer += 1
            cache.remove(city)
            cache.append(city)
                
    return answer