import sys

input = sys.stdin.readline

N = int(input())

# dp_table을 선언
dp_table = [0] * N

# 스케쥴표 정의
schedule_list = [[] for _ in range(N)]
# 완료 기준의 스케쥴표를 입력
for i in range(N):
    time, money = map(int, input().split())
    if i + time - 1 < N:
        schedule_list[i + time - 1].append((time, money))

for i, schedule in enumerate(schedule_list):
    # 스케쥴이 없는 경우
    if len(schedule) == 0:
        # 만약에 첫 날인경우
        if i == 0:
            dp_table[i] = 0
        # 첫날이 아닌 경우에는 이전의 날이 최선이다
        else:
            dp_table[i] = dp_table[i - 1]
    # 스케쥴이 있는 경우
    else:
        # 스케쥴 계산
        sequence = []
        for day, time in schedule:
            sequence.append(dp_table[i - day] + time)
        # 최대값을 dp_table에 할당한다
        dp_table[i] = max(sequence)

print(dp_table[N - 1])