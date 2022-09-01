def solution(sentence):
    answer = len(sentence)

    if answer == 1:
        return answer

    # 1개 단위부터 압축을 시작하여 절반 길이까지 압축시킨다
    for length in range(1, len(sentence) // 2 + 1):
        answer = min(answer, get_encoded_length(sentence, length))

    return answer


# 인코딩된 문자열 길이를 반환해주는 함수
def get_encoded_length(sentence, length):
    current_index, last_index = 0, len(sentence) - 1
    encoded_list = [['', 0]]  # 압축 정보를 담는 배열
    encoded_str = ''  # 압축된 결과

    # 압축 시작
    while current_index <= last_index:
        # 만약 current_index로부터 length만큼 자를수가 없다면?
        if current_index + length >= len(sentence):
            token = sentence[current_index:]
        # length만큼 자를 수 있다면?
        else:
            token = sentence[current_index: current_index + length]
        current_index += length

        # 만약 token이 이전의 내용물과 일치한다면
        if token == encoded_list[-1][0]:
            encoded_list[-1][1] += 1
        # 만약 불일치한다면
        else:
            encoded_list.append([token, 1])

    # 더미 데이터 삭제
    encoded_list.pop(0)

    # 압축된 결과물을 할당한다
    for token, num in encoded_list:
        if num == 1:
            encoded_str += token
        else:
            encoded_str += (str(num) + token)

    return len(encoded_str)