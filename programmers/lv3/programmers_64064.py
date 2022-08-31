import copy


# ban_id에 user를 배열로 엮어서 sequence를 반환해주는 함수
def get_sequence(user_id, banned_id):
    sequence = []
    # banned_id -> user_id를 탐색하면서 sequence를 채우는 로직
    for ban in banned_id:
        user_list = []
        for user in user_id:
            is_equals = False
            # 길이가 똑같은 경우에는
            if len(ban) == len(user):
                is_equals = True
                # 각각의 문자를 대조한다
                for ban_token, user_token in zip(ban, user):
                    # 만약에 ban_token이 *인 경우에는 비교를 패스한다
                    if ban_token == '*':
                        continue
                    # ban_token이 문자인 경우에는 비교를 수행한다
                    else:
                        if ban_token != user_token:
                            is_equals = False

            # 만약에 일치했다면 user_list에 더해준다
            if is_equals == True:
                user_list.append(user)

        # sequence에 반영한다
        sequence.append([ban, user_list])

    return sequence


# 재귀함수를 기반으로 sequence를 탐색하는 함수
# count: 현재의 depth, sequence: 주어진 sequence, user_list: 유저의 목록
# result: 현재 탐색한 user의 집합, result_list: 모든 탐색 결과를 저장하는 배열
def func(count, sequence, user_list, result, result_list):
    # 만약에 탈출 조건을 만족하는 경우 -> 모든 banned list를 탐색 완료한 경우
    if count == len(sequence):
        tmp = copy.deepcopy(result)
        result_list.append(tmp)
        return

    # 순차적으로 계속 탐색
    ban_id, target_list = sequence[count]  # count index에 해당하는 [ban, user_list]를 탐색

    # user를 한명씩 돌면서 ban에 binding 시킨다
    for target in target_list:
        # 우선 target이 user_list에 계신지 확인부터 해야한다
        if target not in user_list:
            continue

        # 우선 result에 target을 집어넣고, user_list에서는 해당 target을 제외시켜버린다
        result.add(target)
        user_list.pop(user_list.index(target))  # user에는 중복이 없기 때문에 가능
        func(count + 1, sequence, user_list, result, result_list)  # depth를 1 늘려서 탐색
        # 탐색을 완료한 다음에는 복구시켜야한다
        result.remove(target)
        user_list.append(target)


def solution(user_list, banned_list):
    result_list = []

    # banned_id, dup_num, listOf(user_id)를 저장
    sequence = get_sequence(user_list, banned_list)

    # 재귀함수 호출
    func(0, sequence, user_list, set(), result_list)

    dup = result_list.count(result_list[-1])

    return len(result_list) // dup