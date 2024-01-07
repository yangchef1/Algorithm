def solution(answers):
    answer = []
    scores = [0,0,0]
    first = [1,2,3,4,5]
    second = [2,1,2,3,2,4,2,5]
    third = [3,3,1,1,2,2,4,4,5,5]
    for i in range(len(answers)):
        if answers[i] == first[i%len(first)]:
            scores[0] += 1
        if answers[i] == second[i%len(second)]:
            scores[1] += 1
        if answers[i] == third[i%len(third)]:
            scores[2] += 1
            
    max_score = max(scores)
    for i in range(len(scores)):
        if scores[i] == max_score:
            answer.append(i + 1)
    return answer