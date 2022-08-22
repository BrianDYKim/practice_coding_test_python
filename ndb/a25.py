def solution(N, stages):
    answer = []
    length = len(stages) # 사용자의 수

    # 모든 stage를 탐색한다
    for i in range(1, N + 1):
        count = stages.count(i) # 해당 stage에 머무르는 사람의 수

        # 만일 count가 0인 경우 (i.e. 모두 통과한 경우)
        if count == 0:
            fail = 0
        # 만일 머무르는 사람이 있는 경우
        else:
            fail = count / length

        length -= count # length 줄이기
        answer.append((fail, i))

    # 정렬
    answer = sorted(answer, key=lambda x: x[0], reverse=True)
    answer = [i[1] for i in answer]

    return answer