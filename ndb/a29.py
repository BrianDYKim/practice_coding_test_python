import sys
input = sys.stdin.readline

N, C = map(int, input().split())
house_list = []

for _ in range(N):
    house_list.append(int(input()))

# 이진 탐색 활용을 위해서 정렬
house_list.sort()

# 이진 탐색을 위해서 최소 갭, 최대 갭을 선언
first = 1
second = house_list[N - 1] - house_list[0]

# 이진 탐색 시작
while first <= second:
    mid = (first + second) // 2
    now = house_list[0] # 첫번째 집부터 설치한다
    count = 1 # 첫번째 집부터 설치하기 때문에 count = 1

    # 집을 순차적으로 방문한다
    for i in range(1, N):
        # gap을 만족하면 설치한다
        if house_list[i] >= now + mid:
            now = house_list[i]
            count += 1

    # count 수에 따라서 first, second 조절
    # C개보다 더 적게 설치가 되면 범위를 더 좁힐 필요가 있음 -> second를 줄인다
    if count < C:
        second = mid - 1
    else:
        first = mid + 1

print(second)