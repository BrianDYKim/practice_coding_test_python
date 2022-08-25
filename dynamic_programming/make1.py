# 1로 만들기
import sys

input = sys.stdin.readline

dp_table = [0] * 30001  # 1부터 30000까지의 결과를 임시 저장
N = int(input().strip())

# 다이내믹 프로그래밍 방식으로 미리 연산
for i in range(2, 30001):
    # 1을 빼는 경우
    dp_table[i] = dp_table[i - 1] + 1
    # 2로 나누어 떨어지는 경우
    if i % 2 == 0:
        dp_table[i] = min(dp_table[i // 2] + 1, dp_table[i])
    # 3으로 나누어 떨어지는 경우
    elif i % 3 == 0:
        dp_table[i] = min(dp_table[i // 3] + 1, dp_table[i])
    # 5로 나누어 떨어지는 경우
    elif i % 5 == 0:
        dp_table[i] = min(dp_table[i // 5] + 1, dp_table[i])

# 결과 출력
print(dp_table[N])