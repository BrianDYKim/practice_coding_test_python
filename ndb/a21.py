import sys
from collections import deque

input = sys.stdin.readline


# bfs 탐색을 통해서 연합을 탐색하는 함수
def bfs(graph, start):
    queue = deque()
    sequence = [start]  # 동맹 정보를 임시 저장하는 배열
    # 방문 처리 후에 큐에 집어넣는다
    visited[start[0]][start[1]] = True
    queue.append(start)

    # 큐가 빌 때까지 반복한다
    while queue:
        v = queue.popleft()
        for direction in direction_vectors:
            # 좌표 정보
            x = direction[0] + v[0]
            y = direction[1] + v[1]
            # 올바른 좌표인가? 그리고 방문한 적이 없는가?
            if 0 <= x < N and 0 <= y < N and not visited[x][y]:
                # 인구 차이가 수지가 맞는다면 -> 방문 처리 시키고 큐에 넣고, sequence에 추가
                v_population = graph[v[0]][v[1]]
                new_population = graph[x][y]
                if L <= abs(v_population - new_population) <= R:
                    visited[x][y] = True
                    queue.append((x, y))
                    sequence.append((x, y))

    alliance_list.append(sequence)


# 모든 나라를 돌면서 동맹을 찾아주는 함수
def check(graph):
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                bfs(graph, (i, j))


# visited, alliance를 초기화시켜버리는 함수
def initialize():
    global alliance_list
    alliance_list = []
    for i in range(N):
        for j in range(N):
            visited[i][j] = False


# allance 배열을 보면서 나라의 인구를 모두 계산해버리는 함수
def calculate_population(graph, alliance_list):
    global ans
    for alliance in alliance_list:
        sum = 0
        for nation in alliance:
            sum += graph[nation[0]][nation[1]]
        sum = sum // len(alliance)
        for nation in alliance:
            graph[nation[0]][nation[1]] = sum
    ans += 1


# 실행 함수
def func(graph):
    # 모든 지도 상의 나라를 돌면서 탐색
    check(graph)
    while len(alliance_list) != N ** 2:
        calculate_population(graph, alliance_list)  # 인구 이동
        initialize()
        check(graph)


# 지도의 크기, L, R 입력
N, L, R = map(int, input().split())
# 지도 정보
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

# 연합 정보를 저장하는 배열
alliance_list = []
# 방문 여부를 저장하는 배열
visited = [[False] * N for _ in range(N)]
# 방향 정보
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
direction_vectors = list(zip(dx, dy))

ans = 0

# 모든 실행
func(graph)

print(ans)
