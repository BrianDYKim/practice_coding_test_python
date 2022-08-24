# 1300 -> K번째 수
import sys

input = sys.stdin.readline

N = int(input())
K = int(input())

# 검색 범위 정의
first, second = 1, min(10 ** 9, N ** 2)
ans = 0

# 이분 탐색 시작
while first <= second:
    mid = (first + second) // 2 # 구하고자하는 숫자
    count = 0

    # 모든 행 순회
    for i in range(1, N + 1):
        temp = mid // i # 해당하는 i 행에 mid 보다 작거나 같은 수가 몇개 있는지?
        sum_factor = temp if temp < N else N # 만약에 temp가 N을 넘어서면 최대가 N개 이기 때문에 N을 반영함
        count += sum_factor

    # count 값 조사
    if count >= K:
        ans = mid
        second = mid - 1
    else:
        first = mid + 1

print(ans)