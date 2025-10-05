import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    
    l = len(food_times)
    
    foods = []
    for i in range(l):
        heapq.heappush(foods, (food_times[i], i + 1))
    
    cur_time = 0
    cycle = 0
    
    while cur_time + ((len(foods) + 1) * (foods[0][0] - cycle)) <= k:
        t, i = heapq.heappop(foods)
        cur_time += ((len(foods) + 1) * (t - cycle))
        cycle = t
    
    foods.sort(key=lambda x : x[1])
    return foods[(k - cur_time) % len(foods)][1]