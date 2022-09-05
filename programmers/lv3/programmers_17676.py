# 시간을 초 단위로 바꿔주는 함수
def transform_time_to_second(time):
    hour, minute, second = time.split(':')
    hour = int(hour) * 3600
    minute = int(minute) * 60
    second = float(second)

    return hour + minute + second


# 주어진 로그를 [시작 시간, 종료 시간]으로 변환시키는 함수
def transform_log(log):
    # date, end_time, process_time 순서로 분리
    date, end_time, process_time = log.split()
    # end_time을 초 단위로 변환
    end_time = transform_time_to_second(end_time)
    # process_time을 실수로 변환
    process_time = process_time[:len(process_time) - 1]
    process_time = float(process_time)
    # process_time을 기반으로 시작 시간을 계산
    start_time = end_time - process_time + 0.001
    # start_time이 음수인 경우 0으로 보정한다
    start_time = 0.0 if start_time < 0 else start_time

    # 1000ms 까지만 단위를 표시하도록한다
    start_time = int(start_time * 1000) / 1000
    end_time = int(end_time * 1000) / 1000

    return [start_time, end_time]


# 주어진 시간 범위 안에 해당 log가 프로세싱 중인지 판단해주는 함수
def is_processing(log, first, second):
    log_first, log_second = log

    # 아예 왼쪽으로 빠져있으면 프로세싱중이 아니다
    if log_first < first and log_second < first:
        return False
    # 아예 오른쪽으로 빠져있으면 프로세싱중이 아니다
    elif log_first > second and log_second > second:
        return False

    # 그 외의 경우 걸쳐있기라도 하기 때문에 True 반환
    return True


# 소수점이 유실되지 않게 덧셈을 처리하는 함수
def safe_add(time, unit):
    time = time * 1000
    unit = unit * 1000

    return (time + unit) / 1000


def solution(lines):
    answer = 0
    # log들의 타임스탬프를 저장한다 (시작 시간, 종료 시간)
    timetable = []
    for log in lines:
        tmp = transform_log(log)
        timetable.append(tmp)

    for time in timetable:
        count = 0
        # 시작 시간 기준으로 first, second를 매긴다
        first, second = time[0], safe_add(time[0], 0.999)
        # 순차 탐색
        for i in range(len(timetable)):
            if is_processing(timetable[i], first, second):
                count += 1

        # answer을 갱신한다
        answer = max(answer, count)
        count = 0

        # 끝 시간을 기준으로 first, second를 매긴다
        first, second = time[1], safe_add(time[1], 0.999)
        # 순차탐색
        for i in range(len(timetable)):
            if is_processing(timetable[i], first, second):
                count += 1

        # answer을 갱신한다
        answer = max(answer, count)

    return answer