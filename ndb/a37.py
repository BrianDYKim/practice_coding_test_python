import sys

input = sys.stdin.readline
INF = int(1e9)

# 도시의 개수
n = int(input())
# 간선의 개수
m = int(input())
# 거리 정보
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# (k, k) 좌표의 경우 자기 자신이므로 0으로 초기화
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0

# 간선 정보 입력
for i in range(m):
    # a->b 코스트가 c라는 뜻
    a, b, c = map(int, input().split())
    # 기존 노선이 갱신되는 경우 최소로 갱신해준다
    graph[a][b] = min(graph[a][b], c)

# 점화 관계를 이용해서 플로이드-워셜 알고리즘 구현
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 출력
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == INF:
            print(0, end=' ')
        else:
            print(graph[i][j], end=' ')
    print()