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

for schedule in schedule_list:
    print(schedule)