import sys

input = sys.stdin.readline
dp_table = [0] * 100

N = int(input())
arr = list(map(int, input().split()))

# 미리 계산
dp_table[0] = arr[0]
dp_table[1] = max(arr[0], arr[1])

# 다이나믹 프로그래밍 방식으로 계산
for i in range(2, N):
    dp_table[i] = max(dp_table[i - 1], dp_table[i - 2] + arr[i])

print(dp_table[N - 1])