def solution(triangle):
    # 2층부터 맨 아래 층까지 읽는다
    for i in range(1, len(triangle)):
        current_floor = triangle[i]
        before_floor = triangle[i - 1]

        for i, current in enumerate(current_floor):
            # leftmost index -> add by before[i]
            if i == 0:
                current_floor[i] = current + before_floor[i]
            elif i == len(current_floor) - 1:
                current_floor[i] = current + before_floor[i - 1]
            else:
                current_floor[i] = current + max(before_floor[i - 1], before_floor[i])

    # 마지막 층에서의 최댓값을 출력한다
    return max(triangle[-1])