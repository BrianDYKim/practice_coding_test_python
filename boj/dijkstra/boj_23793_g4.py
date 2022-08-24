import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

# 정점, 간선의 수
N, M = map(int, input().split())
# 연결 정보
graph = [[] for _ in range(N + 1)]
# 연결 정보 초기화
for i in range(M):
    # a->b 코스트가 c 라는 뜻
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

# X, Y, Z 입력
x, y, z = map(int, input().split())
# 최단거리 정보를 저장하는 배열 선언
distance_x = [INF] * (N + 1) # x 기준으로 최단거리를 계산
distance_y = [INF] * (N + 1) # y 기준으로 최단거리를 계산

# 단순 다익스트라
def simple_dijkstra(start, distance):
    q = []
    # 시작 지점에 대해서 초기화
    distance[start] = 0
    heapq.heappush(q, (0, start))

    # 큐가 빌 때까지 반복한다
    while q:
        dist, now = heapq.heappop(q)
        # 만약에 방문한 경우 패스한다
        if distance[now] < dist:
            continue
        # 방문하지 않은 경우 연결 노드를 모두 조회해서 업데이트한다
        for info in graph[now]:
            # 새로운 코스트 계산
            cost = distance[now] + info[1]
            # 만약 더 짧은 코스트일 경우
            if cost < distance[info[0]]:
                distance[info[0]] = cost
                heapq.heappush(q, (cost, info[0]))

# 중간에 y를 거치지 않는 최단거리를 계산하는 다익스트라 알고리즘
def complex_dijkstra(start, pass_node, distance):
    q = []
    # 시작 지점에 대해서 초기화
    distance[start] = 0
    heapq.heappush(q, (0, start))

    # 큐가 빌 때까지 반복한다
    while q:
        dist, now = heapq.heappop(q)
        # 만약에 방문한 경우거나 아니면 패스해야할 노드의 경우 계산하지 않는다
        if distance[now] < dist or now == pass_node:
            continue
        # 방문하지 않은 경우 연결 노드를 모두 조회해서 업데이트한다
        for info in graph[now]:
            # 새로운 코스트 계산
            cost = distance[now] + info[1]
            # 만약 더 짧은 코스트일 경우
            if cost < distance[info[0]]:
                distance[info[0]] = cost
                heapq.heappush(q, (cost, info[0]))

simple_dijkstra(x, distance_x) # x 기준으로 최단거리를 계산
simple_dijkstra(y, distance_y) # y 기준으로 최단거리를 계산

ans1 = distance_x[y] + distance_y[z] if distance_x[y] != INF and distance_y[z] != INF else -1

distance_x = [INF] * (N + 1)

complex_dijkstra(x, y, distance_x)
ans2 = distance_x[z] if distance_x[z] != INF else -1

print(ans1, ans2)