def solution(N, stages):
    answer = []
    length = len(stages)

    # 스테이지를 1부터 N까지 조회한다
    for i in range(1, N + 1):
        # 해당 스테이지에 있는 사람의 수를 센다
        count = stages.count(i)

        if count == 0:
            fail = 0
        else:
            fail = count / length

        answer.append((i, fail))
        length -= count

    answer = sorted(answer, key=lambda x: x[1], reverse=True)
    answer = [i[0] for i in answer]

    return answer