def solution(s):
    answer = []
    sequence = []  # 뽑아낸 문자열에서 추출되는 배열을 저장하는 list

    # 우선 맨 앞, 맨 뒤의 {}를 삭제시킨다
    first_str = s[1:-1]
    # 순차적으로 읽으면서 {}사이의 문자열을 추출해버린다
    first_idx, second_idx = 0, 0
    for i in range(len(first_str)):
        # 집합의 시작 인덱스인 경우
        if first_str[i] == '{':
            first_idx = i
        # 집합의 끝 인덱스인 경우
        elif first_str[i] == '}':
            second_idx = i  # second_idx를 할당한다
            # first_idx, second_idx 사이의 문자열을 뽑아내야한다
            target = first_str[first_idx + 1:second_idx]
            # 뽑아낸 문자열을 기반으로 list를 추출한다
            target_list = list(map(int, target.split(',')))
            # sequence에 append 시킨다
            sequence.append(target_list)

    # len 순서대로 정렬한다
    sequence = sorted(sequence, key=lambda x: len(x))

    # sequence를 순차로 읽으면서 answer에 append 시킨다
    for item in sequence:
        # 만약에 첫번째 원소라면?
        if len(item) == 1:
            answer.append(item[0])
        # 나머지 원소일 경우
        else:
            for num in item:
                if num not in answer:
                    answer.append(num)
                    break

    return answer