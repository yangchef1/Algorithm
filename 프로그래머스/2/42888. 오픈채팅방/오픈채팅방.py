def solution(record):
    answer = []

    meta = {}
    index = {}
    history = []
    
    for r in record:
        if r.startswith('Enter'):
            behave, uid, name = r.split()
            for i in index.get(uid, []):
                history[i][0] = name
            meta[uid] = name
            history.append([name, '님이 들어왔습니다.'])
            index[uid] = index.get(uid, []) + [len(history) - 1] 
        elif r.startswith('Leave'):
            behave, uid = r.split()
            history.append([meta[uid], '님이 나갔습니다.'])
            index[uid] = index.get(uid, []) + [len(history) - 1]
        else:
            behave, uid, name = r.split()
            meta[uid] = name
            for i in index[uid]:
                history[i][0] = name
    
    for h in history:
        answer.append(''.join(h))
    
    return answer