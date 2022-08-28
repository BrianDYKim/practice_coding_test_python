def solution(arr):
    answer = []
    for num in arr:
        if len(answer) == 0:
            answer.append(num)
        else:
            temp = answer[-1]
            if num != temp:
                answer.append(num)

    return answer