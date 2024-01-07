def solution(sizes):
    max_width, max_height = 0, 0

    for size in sizes:
        max_width = max(max_width, max(size))
        max_height = max(max_height, min(size))

    return max_width * max_height
