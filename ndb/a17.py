import sys
import copy
sys.setrecursionlimit(100000)
input = sys.stdin.readline

N, K = map(int, input().split()) # 맵의 크기 N, 바이러스 가짓수 K
graph = [] # 지도 정보

# 지도 정보 입력
for _ in range(N):
    info = list(map(int, input().split()))
    graph.append(info)

S, x, y = map(int, input().split()) # 바이러스가 증식하는 초 S, 원하는 좌표 X, Y
virus_info = [] # 바이러스 감염 정보를 저장하는 리스트

# 바이러스 정보 입력
for i in range(N):
    for j in range(N):
        if graph[i][j] != 0:
            virus_info.append((graph[i][j], i, j))

virus_info.sort(key=lambda x: x[0])

# 답을 구하는 함수
def solution(count):
    # 탈출 조건: 해당 좌표가 감염이 되어있거나, 혹은 count가 N이 되어버리는 경우
    if count == S or graph[x - 1][y - 1] != 0:
        print(graph[x - 1][y - 1])
        return

    temp = copy.deepcopy(virus_info)
    # virus_info를 선형으로 읽으면서 동작 수행
    for virus in temp:
        vx, vy = virus[1], virus[2] # 바이러스의 좌표
        coordinate_list = [(vx - 1, vy), (vx + 1, vy), (vx, vy - 1), (vx, vy + 1)] # 전파할 좌표들

        for coordinate in coordinate_list:
            if 0 <= coordinate[0] < N and 0 <= coordinate[1] < N and graph[coordinate[0]][coordinate[1]] == 0:
                graph[coordinate[0]][coordinate[1]] = virus[0] # 전염
                virus_info.append((virus[0], coordinate[0], coordinate[1]))

    virus_info.sort(key=lambda x: x[0])
    solution(count + 1)

solution(0)