import sys
import copy
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def ans(graph, depth):
    global answer
    if depth == 3:
        copied_graph = copy.deepcopy(graph)
        safe = 0

        # dfs 탐색
        for i in range(N):
            for j in range(M):
                if copied_graph[i][j] == 2:
                    dfs(copied_graph, i, j)

        for i in range(N):
            for j in range(M):
                if copied_graph[i][j] == 0:
                    safe += 1
        answer = max(answer, safe)
        return

    for i in range(N):
        for j in range(M):
            # 빈 칸을 발견하면
            if graph[i][j] == 0:
                graph[i][j] = 1  # 벽을 세우고
                ans(graph, depth + 1)  # 더 탐색한다
                graph[i][j] = 0  # 벽을 해제한다

# dfs 기반으로 탐색
# 지도를 탐색하면서 바이러스를 마주치면 dfs 탐색을 수행하면된다
# 방문 처리(2로 수정) -> 상하좌우를 탐색하면서 나아감
def dfs(graph, x, y):
    # 상하좌우를 모두 감염 처리시킴
    # 상하좌우를 dfs 탐색 시킴
    coordinate_list = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

    for coordinate in coordinate_list:
        if 0 <= coordinate[0] < N and 0 <= coordinate[1] < M and graph[coordinate[0]][coordinate[1]] == 0:
            graph[coordinate[0]][coordinate[1]] = 2
            dfs(graph, coordinate[0], coordinate[1])

N, M = map(int, input().split()) # N, M 입력
answer = 0
# 지도 선언
graph = []

# 지도 정보 입력
for _ in range(N):
    info = list(map(int, input().split()))
    graph.append(info)

ans(graph, 0)
print(answer)