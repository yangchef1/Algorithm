def solution(N, stages):
    answer = []
    fail = {i : [0, 0] for i in range(1, N + 1)}
    
    for stage in stages:
        for i in range(stage if stage < N + 1 else stage - 1, 0, -1):
            fail[i][1] += 1
        if stage < N + 1:
            fail[stage][0] += 1

    result = list(fail.items())
    result.sort(key=lambda x: (x[1][0] / x[1][1]) if x[1][1] != 0 else 0, reverse=True)
    
    answer = list(map(lambda x: x[0], result))
    return answer