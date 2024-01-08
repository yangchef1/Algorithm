from itertools import permutations

def solution(k, dungeons):
    for i in range(len(dungeons), 1, -1):
        for permutation in permutations(dungeons, i):
            temp_k = k
            is_completed = True
            for dungeon in permutation:
                if dungeon[0] <= temp_k:
                    temp_k -= dungeon[1]
                else:
                    is_completed = False
            if is_completed:
                return len(permutation)
    return 0