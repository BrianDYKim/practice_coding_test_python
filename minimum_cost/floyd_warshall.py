import sys

input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수
n, m = map(int, input().split())
# 인접 행렬
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신으로 가는 경우를 모두 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 간선 정보 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 점화식을 이용해서 플로이드-워셜 알고리즘 작성
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 결과 출력
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == INF:
            print('INF', end=' ')
        else:
            print(graph[i][j], end=' ')
    print()