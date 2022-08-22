import sys
input = sys.stdin.readline

N = int(input())
my_list = list(map(int, input().split()))

first, second = 0, N - 1

while first <= second:
    mid = (first + second) // 2

    # my_list[mid]가 mid보다 큰 경우에는 끝점을 좁힌다
    # 역으로 작은 경우에는 시작점을 올려준다
    # 일치하는 경우? 프린트
    if my_list[mid] == mid:
        print(mid)
        break
    elif my_list[mid] > mid:
        second = mid - 1
    else:
        first = mid + 1

if first > second:
    print(-1)