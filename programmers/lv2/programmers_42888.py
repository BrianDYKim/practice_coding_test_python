def solution(record_list):
    answer = []
    record_dict = {}  # key: user_id, value: nickname

    for record in record_list:
        token_list = list(record.split())  # 띄어쓰기로 구분된 토큰을 리스트로 분리시켜버린다

        # 명령 종류별로 분기시킨다
        # 입장시에는 dict를 업데이트 시키고, answer에다가 기록을 더한다
        if token_list[0] == 'Enter':
            record_dict[token_list[1]] = token_list[2]  # user_id : nickname 쌍 최신화
            answer.append((token_list[1], '님이 들어왔습니다.'))  # 기록 추가
        # 퇴장시에는 answer에다가 기록만 더한다
        elif token_list[0] == 'Leave':
            answer.append((token_list[1], '님이 나갔습니다.'))
        # 닉네임 변경시에는 dict만 업데이트한다
        elif token_list[0] == 'Change':
            record_dict[token_list[1]] = token_list[2]

    # answer을 갱신한다
    answer = [record_dict[user_id] + message for user_id, message in answer]


    return answer