import sys

input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수
n, m = map(int, input().split())
# 최단 거리 테이블
distance = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신의 경우는 0으로 초기화
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            distance[i][j] = 0

# 간선 정보 입력
for _ in range(m):
    src, dest = map(int, input().split())
    # 양방향 간선으로 초기화
    distance[src][dest] = 1
    distance[dest][src] = 1

# 점화식을 이용한 플로이드-워셜 알고리즘 구현
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            distance[a][b] = min(distance[a][b], distance[a][k] + distance[k][b])

# 최종 목적지, 중간 목적지
x, k = map(int, input().split())

# 걸리는 시간
ans = distance[1][k] + distance[k][x] if distance[1][k] != INF and distance[k][x] != INF else -1

print(ans)