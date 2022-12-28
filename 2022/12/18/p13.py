# 실전 13번 문제 (제한 시간 1초)
import sys
input = sys.stdin.readline

answer = 1e9 # 치킨거리를 저장하는 변수

# N: 도시의 행과 열 정보(50), M: 선택하는 치킨집의 개수(13)
N, M = map(int, input().split())
chickenMap = [[0 for i in range(N)] for j in range(N)]

# 치킨맵 입력
for i in range(N):
    tmp = list(map(int, input().split()))
    chickenMap[i] = tmp

# 가정집 위치를 저장하는 배열
houses = []
for i in range(N):
    for j in range(N):
        if chickenMap[i][j] == 1:
            houses.append((i, j)) # 가정집 위치를 모두 저장

# 가정집을 기준으로 치킨거리 합을 반환하는 함수
def getSumOfDistances(chickenHouses):
    result = 0
    for house in houses:
        tmp = []
        houseX, houseY = house

        for chicken in chickenHouses:
            chickenX, chickenY = chicken
            diffX = abs(houseX - chickenX)
            diffY = abs(houseY - chickenY)

            tmp.append(diffX + diffY)

        # tmp에서 최소를 뽑아서 result에 합해준다
        result += min(tmp)

    return result

# 다음 탐색 좌표를 알려주는 함수
def nextCoordinate(x, y):
    y += 1

    if y == N:
        x += 1
        y = 0

    return x, y

def solution(n, x, y, chickenHouses):
    global answer
    if n == M:
        # 치킨거리를 계산해서 answer에 반영한다
        tmp = getSumOfDistances(chickenHouses)
        answer = min(tmp, answer)
        return

    # 끝까지 탐색하지 못하고 범위를 초과하는 경우
    if x == N and y == N:
        return

    # 점화관계
    for i in range(x, N):
        for j in range(N):
            if (i, j) in chickenHouses:
                continue

            # 치킨집인 경우 depth를 추가
            if chickenMap[i][j] == 2:
                chickenHouses.append((i, j))
                newX, newY = nextCoordinate(i, j)
                solution(n + 1, newX, newY, chickenHouses)
                chickenHouses.pop()

solution(0, 0, 0, [])
print(answer)