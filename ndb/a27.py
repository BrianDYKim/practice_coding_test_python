import sys
input = sys.stdin.readline

# 하한을 구하는 함수
def lower_bound(array, target, first, second):
    mid = (first + second) // 2

    # 하한이 존재하지 않는 경우
    if first > second:
        return None

    # 가장 왼쪽 원소인 경우
    if array[mid] == target and (mid == 0 or array[mid - 1] < target):
        return mid
    elif array[mid] >= target:
        return lower_bound(array, target, first, mid - 1)
    else:
        return lower_bound(array, target, mid + 1, second)

# 상한을 구하는 함수
def upper_bound(array, target, first, second):
    mid = (first + second) // 2

    # 상한이 존재하지 않는 경우
    if first > second:
        return None

    # 가장 오른쪽 원소인 경우
    if array[mid] == target and (mid == len(array) - 1 or array[mid + 1] > target):
        return mid
    elif array[mid] <= target:
        return upper_bound(array, target, mid + 1, second)
    else:
        return upper_bound(array, target, first, mid - 1)

N, x = map(int, input().split())
num_list = list(map(int, input().split()))

lower = lower_bound(num_list, x, 0, N - 1)
upper = upper_bound(num_list, x, 0, N - 1)

# 상한, 하한 모두 있는 경우
if lower is not None and upper is not None:
    print(upper - lower + 1)
else:
    print(-1)