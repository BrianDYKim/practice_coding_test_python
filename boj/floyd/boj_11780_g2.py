import sys
import copy

input = sys.stdin.readline
INF = int(1e9)

# 도시의 개수
n = int(input())
# 간선의 개수
m = int(input())
# 연결 정보를 담는 리스트 (distance, )
graph = [[(INF, [])] * (n + 1) for _ in range(n + 1)]

# 자기 자신으로 가는 경우 모두 거리를 0으로 초기화한다
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = (0, [])

# 간선 정보 입력
for i in range(m):
    a, b, c = map(int, input().split())  # a->b 가는 코스트가 c 라는 뜻
    graph[a][b] = (c, [a, b]) if c <= graph[a][b][0] else graph[a][b]

# 플로이드-워셜 알고리즘
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            new_cost = graph[a][k][0] + graph[k][b][0]
            # 새롭게 갱신해야하는 경우 -> (a,k)의 경로에 b로 가는 경로를 append 해서 수정한다
            if new_cost < graph[a][b][0]:
                before_way = copy.deepcopy(graph[a][k][1])
                before_way.append(b)
                graph[a][b] = (new_cost, before_way)

# 비용만 출력
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j][0] == INF:
            print(0, end=' ')
        else:
            print(graph[i][j][0], end=' ')
    print()

# 비용과 경로를 함께 출력
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j][0] == INF:
            print(0)
        else:
            print(len(graph[i][j][1]), *graph[i][j][1])