# 현재 설치된 구조물이 가능한 구조물인지 검증해주는 메소드
def possible(current_list):
    # 하나씩 구조물을 검증하면서 나아간다
    for x, y, stuff in current_list:
        # 설치된 것이 기둥인 경우
        if stuff == 0:
            # 바닥 위, 보의 한쪽 끝, 다른 기둥 위인지 검증하기
            if y == 0 or [x - 1, y, 1] in current_list or [x, y, 1] in current_list or [x, y - 1, 0] in current_list:
                continue
            return False  # 위의 조건에서 안 걸리고 여기를 만나면 불가능한 구조물이다

        # 설치된 것이 보인 경우
        elif stuff == 1:
            # 한쪽 끝 부분이 기둥 위 혹은 양쪽 끝 부분이 다른 보와 동시에 연결이 되어있는 경우 정상
            if [x, y - 1, 0] in current_list or [x + 1, y - 1, 0] in current_list or (
                    [x - 1, y, 1] in current_list and [x + 1, y, 1] in current_list):
                continue
            return False
    return True


def solution(n, build_frame):
    answer = []

    for frame in build_frame:
        x, y, stuff, operate = frame

        # 삭제 명령어의 경우
        if operate == 0:
            answer.remove([x, y, stuff])

            if not possible(answer):
                answer.append([x, y, stuff])

        # 설치 명령어의 경우
        elif operate == 1:
            answer.append([x, y, stuff])
            if not possible(answer):
                answer.remove([x, y, stuff])

    return sorted(answer, key=lambda x: (x[0], x[1], x[2]))