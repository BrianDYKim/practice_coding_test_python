import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수
n, m = map(int, input().split())
# 시작 노드
start = int(input())
# 연결 정보
graph = [[] for i in range(n + 1)]
# 최소 거리 정보
distance = [INF] * (n + 1)

# 모든 간선 정보 입력 받기
for i in range(m):
    a, b, c = map(int, input().split())
    # a에서 b로 가는 코스트는 c이다
    graph[a].append((b, c))

# 다익스트라 구현
def dijkstra(start):
    q = []

    # 시작 노드에 대한 초기화
    distance[start] = 0
    heapq.heappush(q, (0, start))

    # 큐가 빌 때까지 반복
    while q:
        # q에서 하나를 꺼내온다
        dist, now = heapq.heappop(q)
        # 만약 방문한 적이 있으면 건너뛴다
        if distance[now] < dist:
            continue

        # 인접한 노드들을 모두 순회
        for i in graph[now]:
            cost = distance[now] + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print('inf')
    else:
        print(distance[i])