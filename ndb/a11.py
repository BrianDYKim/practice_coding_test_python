# 기둥을 세울수있는지 검증하는 메소드
# 파라미터: 명령어, 현재 현황
def check_pillow(instruction, current_list):
    is_able = False
    coordinate = (instruction[0], instruction[1])  # 가로, 세로 좌표

    # 현재 세워진 기둥의 좌표들을 저장
    current_pillows = list(filter(lambda x: x[2] == 0, current_list))
    current_plates = list(filter(lambda x: x[2] == 1, current_list))

    # 현재 좌표가 바닥 위인가? -> 세로의 좌표가 0이다
    if coordinate[1] == 0:
        is_able = True

    # 보의 한쪽 끝을 가리키는가? -> 보의 좌표에서 가로를 1 더해본게 주어진 좌표랑 일치하면 된다
    for plate in current_plates:
        # 보의 오른쪽 끝 좌표
        plate_coordinate = (plate[0] + 1, plate[1])

        if coordinate == plate_coordinate:
            is_able = True

    # 기둥에서 이어지는 형태인가? -> 기둥의 좌표에서 세로로 1을 더해본게 주어진 좌표랑 일치하면 된다
    for pillow in current_pillows:
        # 기둥의 위쪽 끝 좌표
        pillow_coordinate = (pillow[0], pillow[1] + 1)

        if coordinate == pillow_coordinate:
            is_able = True

    return is_able


# 보를 세울수있는지 검증하는 메소드
def check_plate(instruction, current_list):
    is_able = False
    start_coordinate = (instruction[0], instruction[1])  # 가로, 세로 좌표, 시작점
    end_coordinate = (instruction[0] + 1, instruction[1])  # 가로, 세로 좌표, 끝점

    # 현재 세워진 기둥의 좌표들을 저장
    current_pillows = list(filter(lambda x: x[2] == 0, current_list))
    current_plates = list(filter(lambda x: x[2] == 1, current_list))

    # 한쪽이 기둥이랑 연결이 되어있는가? -> 시작점에 기둥이 있거나, 아니면 오른쪽 끝에 기둥이 있던가
    for pillow in current_pillows:
        # 기둥의 위쪽 끝 좌표
        pillow_coordinate = (pillow[0], pillow[1] + 1)

        if start_coordinate == pillow_coordinate or end_coordinate == pillow_coordinate:
            is_able = True

    first_cond, second_cond = False, False  # 왼쪽, 오른쪽 각각 보가 있는가?

    # 양쪽에 이어지는 보가 있는가?
    for plate in current_plates:

        # 현재 start coordinate에서 가로를 1을 빼면 보가 있는가?
        if start_coordinate[0] - 1 == plate[0] and start_coordinate[1] == plate[1]:
            first_cond = True

        # 현재 end coordinate와 일치하는 보가 있는가?
        if end_coordinate == (plate[0], plate[1]):
            second_cond = True

        # 두 조건을 모두 만족하면 is_able을 True로 전환
        if first_cond == True and second_cond == True:
            is_able = True

    return is_able


# 구조물을 삭제 가능한지 검증하는 메소드 -> 임시로 삭제해보고 위의 메소드를 모조리 호출해보면된다
def check_deletable(instruction, current_list):
    check_builds = []
    # 검증해야될 instruction build를 정의
    check_instruction = [instruction[0], instruction[1], instruction[2]]

    # 깊게 복사
    for current in current_list:
        if current != check_instruction:
            check_builds.append(current)

    # 검증
    for build in check_builds:
        # 설치 명령어를 생성해버린다
        new_instruction = (build[0], build[1], build[2], 1)

        # 기둥인 경우 체크
        if new_instruction[2] == 0:
            if check_pillow(new_instruction, check_builds) == False:
                return False

        # 보인 경우 체크
        if new_instruction[2] == 1:
            if check_plate(new_instruction, check_builds) == False:
                return False

    return True


def solution(n, build_frame):
    current_list = []

    # 명령어를 한 줄씩 읽는다
    for instruction in build_frame:
        constructure = instruction[2]  # 설치하는 종류
        build_ins = instruction[3]  # 설치, 삭제

        # 설치하는 경우 검증
        if build_ins == 1:
            # 기둥인 경우
            if constructure == 0:
                if check_pillow(instruction, current_list) == True:
                    current_list.append([instruction[0], instruction[1], constructure])

            # 보인 경우
            elif constructure == 1:
                if check_plate(instruction, current_list) == True:
                    current_list.append([instruction[0], instruction[1], constructure])

        # 삭제하는 경우 검증
        elif build_ins == 0:
            if check_deletable(instruction, current_list) == True:
                current_list.remove([instruction[0], instruction[1], constructure])

    # 정렬
    current_list.sort()

    return current_list