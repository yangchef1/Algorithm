def compare(size1, size2):
    result = []
    if size1[0] > size2[0]:
        result.append(size1[0])
    else:
        result.append(size2[0])
    
    if size1[1] > size2[1]:
        result.append(size1[1])
    else:
        result.append(size2[1])
        
    return result
    
def solution(sizes):
    answer = 0
    wallet_size = [0, 0]
    for size in sizes:
        if ((wallet_size[0] - size[0]) * (wallet_size[1] - size[1])) > 0:
            wallet_size[0] = max(wallet_size[0], size[0])
            wallet_size[1] = max(wallet_size[1], size[1])
        else:
            not_rotated = compare(wallet_size, size)
            size.reverse()
            rotated = compare(wallet_size, size)
            
            if rotated[0] * rotated[1] > not_rotated[0] * not_rotated[1]:
                wallet_size = not_rotated
            else:
                wallet_size = rotated
        
    answer = wallet_size[0] * wallet_size[1]
    return answer