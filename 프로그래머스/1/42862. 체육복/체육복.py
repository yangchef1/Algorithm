def solution(n, lost, reserve):
    borrow = []
    lost_without_reserve = list(set(lost) - set(reserve))
    reserve_without_lost = list(set(reserve) - set(lost))
    
    for std in lost_without_reserve:
        if (std - 1) in reserve_without_lost:
            borrow.append(std)
            reserve_without_lost.remove(std - 1)
        elif (std + 1) in reserve_without_lost:
            borrow.append(std)  
            reserve_without_lost.remove(std + 1)
    
    return n - len(lost_without_reserve) + len(borrow)